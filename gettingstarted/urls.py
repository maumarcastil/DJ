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
    path("admin/", admin.site.urls),
]
