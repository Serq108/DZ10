# Generated by Django 2.2.1 on 2019-06-11 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_courselist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('dtm', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.CourseList')),
                ('snippet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.Snippet')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]