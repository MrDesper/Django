from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from crud_blog_web.models import Article


# Create your views here.

def index(request):
    return HttpResponse("Napis testowy")

def indexArticle(request):
    articles = Article.objects.all()
    return render(request, 'art.html',{
        'articles': articles,
        "title": title
    })