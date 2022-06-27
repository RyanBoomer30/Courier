from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("member", views.member, name="member"),
    path("articleCreate", views.articleCreate, name="articleCreate"),
    path("article/<int:article_id>", views.article, name="article"),
    path("article/<int:article_id>/editView", views.articleEditView, name="articleEditView"),
    path("article/<int:article_id>/edit", views.articleEdit, name="articleEdit"),
    path("articleView/<str:filter>", views.articleView, name="articleView"),
    path("articleSearch", views.articleSearch, name="articleSearch"),
    path("staff", views.staff, name="staff"),
    path("about", views.about, name="about"),
    path("adminPanel", views.adminPanel, name="adminPanel"),
    path("memberEditChoose", views.memberEditChoose, name="memberEditChoose"),
    path("memberEdit/<int:member_id>", views.memberEdit, name="memberEdit"),
]