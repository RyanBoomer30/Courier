from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django import forms
from django.views.generic import CreateView
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
import json

from .models import *

class addArticle(forms.Form):
    content = forms.CharField(label="Article Content", widget = CKEditorWidget())

class editArticle(ModelForm):
    class Meta:
        model = Article
        fields = ['articleContent','image']

# Main view page
def index(request):
    news = Article.objects.filter(articleCatagory="News").order_by('-createdTime')
    opinions = Article.objects.filter(articleCatagory="Opinions").order_by('-createdTime')
    sports = Article.objects.filter(articleCatagory="Sports").order_by('-createdTime')
    lifestyles = Article.objects.filter(articleCatagory="Lifestyles").order_by('-createdTime')
    arts = Article.objects.filter(articleCatagory="Arts").order_by('-createdTime')
    humors = Article.objects.filter(articleCatagory="Humor").order_by('-createdTime')
    return render(request, "website/index.html", {
        'news': news,
        'opinions': opinions,
        'sports': sports,
        'lifestyles': lifestyles,
        'arts': arts,
        'humors': humors
    })

# Login
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("member"))
        else:
            return render(request, "website/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "website/login.html")

# Logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["name"]
        position = request.POST["position"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "website/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            member = Member.objects.create(user=user, name=name, position=position)
            member.save()
        except IntegrityError:
            return render(request, "website/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "website/register.html")

def member(request):
    if request.user.is_anonymous:
        return render(request, "website/member.html",{
                'status': False,
            })
    else:
        if Member.objects.filter(user=request.user).exists():
            return render(request, "website/member.html",{
                'status': True,
                'member': Member.objects.get(user=request.user),
                'form': addArticle,
            })
        else:
            return render(request, "website/member.html",{
                'status': False,
            })


def articleCreate(request):
    if request.method == "POST":
        name = request.POST["name"]
        content = request.POST["content"]
        catagory = request.POST["catagory"]
        image = request.FILES["image"]
        credit = request.POST["credit"]
        user = Member.objects.get(user=request.user)
        article = Article.objects.create(
            articleName=name, 
            articleContent=content, 
            articleCatagory=catagory, 
            writer=user,
            image=image,
            imageCredit=credit)
        article.save()
        return HttpResponseRedirect(reverse("member"))

def articleView(request, filter):
    # if Article.objects.filter(articleCatagory=filter).exists():
    articles = Article.objects.filter(articleCatagory=filter)
    members = Article.objects.filter(writer__name=filter)
    return render(request, "website/articlesView.html",{
        'articles': articles,
        'members': members,
    })

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, "website/article.html",{
        'article': article,
    })

def articleEditView(request, article_id):
    article = Article.objects.get(id=article_id)
    if (article.writer.user == request.user):
        form = editArticle(instance=article)
        return render(request, "website/articleEdit.html",{
            'article': article,
            'form': form
        })
    return HttpResponse("What u trying to pull here? Don't go edit random articles")

def articleEdit(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        article.articleName = request.POST["name"]
        article.articleCatagory = request.POST["catagory"]
        article.imageCredit = request.POST["credit"]
        article.save()
        editedForm = editArticle(request.POST, request.FILES, instance=article)
        if editedForm.is_valid():
            editedForm.save()
        return HttpResponseRedirect(reverse("index")) 

def articleSearch(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        articles = Article.objects.filter(articleName__contains=searched)
        writers = Article.objects.filter(writer__name__contains=searched)
        return render(request, "website/articlesView.html",{
            'articles': articles,
            'writers': writers,
        })

def staff(request):
    chief = Member.objects.filter(position="Chief")
    section = Member.objects.filter(position="Section")
    graphic = Member.objects.filter(position="Graphic")
    writer = Member.objects.filter(position="Staff")
    artist = Member.objects.filter(position="Artist")
    photographer = Member.objects.filter(position="Photographer")
    return render(request, "website/staff.html", {
        'chief':chief,
        'section':section,
        'graphic':graphic,
        'writer':writer,
        'artist':artist,
        'photographer':photographer,
    })

def about(request):
    return render(request, "website/about.html")