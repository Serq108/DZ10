from rest_framework import serializers
from snippets.models import Snippet, CourseList, CoursePage
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from tutorial.settings import BASE_URL
from utils.token_generator import token_generator, create_email_confirm_url

# class SnippetSerializer(serializers.ModelSerializer):
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        # fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
        fields = ('url', 'id', 'title', 'owner')


class CreateSnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = (
            'url', 'id', 'title', 'code', 'linenos', 'language',
            'style', 'owner', 'perm_list'
        )


# class UserSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            is_active = False,
            email = validated_data['email']
        )
        print('SOMEPRINT',validated_data)
        print('SOMEPRINT')
        token = token_generator.make_token(user)
        url = create_email_confirm_url(user.id, token)
        print('SOMEPRINT', url)
        # ~ send_mail(
            # ~ 'Activation on Django', url, 'djangodev108@gmail.com',
            # ~ [validated_data['email']], fail_silently=False
        # ~ )
        user.set_password(validated_data['password'])
        user.groups.add(1)
        user.save()
        if User.objects.filter(username=self.validated_data['username']).exists():
            send_mail(
                'Activation on Django', url, 'djangodev108@gmail.com',
                [validated_data['email']], fail_silently=False
            )
        else:
            print('SOMEPRINT wrong')
        return user

    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'email', 'first_name',
            'last_name',
        )


class CreateCourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CourseList
        fields = ('title', 'descrpt', 'owner')


class CreateCoursePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePage
        fields = ('course', 'snippet', 'order', 'dtm')


class CourseListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseList
        fields = ('url', 'id', 'title', 'descrpt', 'owner')


class CoursePageSerializer(serializers.HyperlinkedModelSerializer):
    # snippet = serializers.HyperlinkedRelatedField(many=False, view_name='snippet-detail', read_only=True)
    title = serializers.ReadOnlyField(source='snippet.title')
    class Meta:
        model = CoursePage
        fields = ('order',  'title', 'dtm','snippet')


class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    # pages = serializers.StringRelatedField(many=True)
    # pages_listing = serializers.HyperlinkedIdentityField(view_name='coursepage-list')
    pages = CoursePageSerializer(many=True, read_only=True)
    # ~ pages = serializers.HyperlinkedRelatedField(
        # ~ many=True,
        # ~ view_name='coursepage-detail',
        # ~ read_only=True
    # ~ )

    class Meta:
        model = CourseList
        fields = ('title', 'descrpt', 'pages')


class CourseDetailPageSerializer(serializers.HyperlinkedModelSerializer):
    # pages = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    title = serializers.ReadOnlyField(source='snippet.title')

    class Meta:
        model = CoursePage
fields = ('title', 'order', 'dtm', 'snippet')
