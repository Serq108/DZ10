# DZ10
Добавление фич для сайта с курсами
Базовый бэк энд для сайта с курсами
1. На нашем ресурсе есть админ, преподаватели Tutors,
студенты Students. 
2. преподавателей может регистрировать только админ,
преподаватели могут постить снипетты , просматривать их 
изменять и удалять могут только свои сниппеты, сниппеты это куски кода 
с описанием.
3. Студентов может регистрировать любой аноним, студенты могут 
просматривать списки всех  пользователей , и списки сниппетов ,
но могут просматривать детали сниппета. Удалять студентов может только 
админ.

4. В проекте сделать так чтобы тьюторы могли формировать сами 
список студентов допустимых  к просмотру конкретного сниппета.
но только на свои сниппеты. 
5. Добавлено подтверждение регистрации на сайте с помощью электронной почты  

логин: admin pass: 123

Список ресурсов:

    path('snippets/',просмотр списка сниппетов

    path('snippets/create/' создание сниппета

    path('snippets/<int:pk>/', детали сниппета

    path('users/'просмотр списка юзеров

    path('users/<int:pk>/', информация о юзере

    path('reg/', регистрация студентов
