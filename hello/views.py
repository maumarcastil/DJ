from django.shortcuts import render
from django.http import HttpResponse

# Imports Models
from hello.models import Article, Category


# My Index
def index(request):

    years = range(2000, 2051)

    return render(request, "index.html",{
        'title': "Index V",
        'year': years,
    })

def helloworld(request):
    return render(request, "hello_world.html")


""" def create_article(request):
    article = Article(
        title = "primer articulo",
        content ="Este es el contenido",
        public = True
    )
    article.save()


    return HttpResponse("Create Article success  <br> Title: {} <br> Content: {}".format(article.title, article.content))
 """

def create_article(request, title, content):
    article = Article(
        title = title,
        content = content,
        public = True
    )
    article.save()


    return HttpResponse("Create Article success  <br> Title: {} <br> Content: {}".format(article.title, article.content))


def get_article(request):
    article = Article.objects.get(pk=5)

    return HttpResponse("articulo: {}, {}, {}".format(article.title, article.content, article.public))

def update_article(request, id):

    try:
        article = Article.objects.get(pk=id)
        article.title = "Este es el titulo editado"
        article.content = "Eeste es el contenido editado"
        article.public = False
        article.save()
        response = "Article edit success"
    except:
        response = "Article edit <strong>ERROR</strong>"
    

    return HttpResponse(response)


