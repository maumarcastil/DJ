from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

urlpatterns = [
    path("", hello.views.index, name="Index"),
    path("helloworld/", hello.views.helloworld, name="helloworld"),
    path("create_article/<str:title>/<str:content>/", hello.views.create_article, name="create_article"),
    path("get_article/", hello.views.get_article, name="get_article"),
    path("update_article/<str:id>/", hello.views.update_article, name="update_article"),
    path("list_articles/", hello.views.list_articles, name="list_articles"),
    path("delete_article/<str:id>/", hello.views.delete_article, name="delete_article"),

# Formularios GET & POST
    path("add_article_form/", hello.views.add_article_form, name="add_article_form"),
    path("create_article_form/", hello.views.create_article_form, name="create_article_form"),

    path("admin/", admin.site.urls),
]
