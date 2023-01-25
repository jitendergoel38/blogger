import factory

from django.contrib.auth.models import User

from djblogger.blog.models import Blog


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = "x"
    subtitle = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    status = "published"
