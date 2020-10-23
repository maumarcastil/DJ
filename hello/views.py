from django.shortcuts import render, redirect
from django.http import HttpResponse

# Imports Models
from hello.models import Article, Category


# My Index
def index(request):

    years = range(2000, 2051)

    return render(request, "index.html", {
        'title': "Index V",
        'year': years,
    })


def helloworld(request):
    return render(request, "hello_world.html")


def create_article(request, title, content):
    article = Article(
        title=title,
        content=content,
        public=True
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


def list_articles(request):

    articles = Article.objects.filter(valid=True)
    #articles = Article.objects.filter().exclude(public = False)

    # This Is For Make Querys
    #articles = Article.objects.raw()

    return render(request, "article.html", {
        'articles': articles
    })


def delete_article(request, id):

    article = Article.objects.get(pk=id)
    article.valid = False
    article.save()

    return redirect("list_articles")


# Formularios GET & POST

def add_article_form(request):

    return render(request, "create_article_form.html")


def create_article_form(request):
    try:
        if request.method == "GET":
            title = request.GET["title"]
            content = request.GET["content"]
            public = request.GET["public"]

            article = Article(
                title=title, 
                content=content, 
                public=public,
                valid = True
                )        
            article.save()

            #return HttpResponse("<h3>Articulo creado con exito</h3>")
            return redirect("add_article_form")
    except:
        return HttpResponse("<h3>No se ah podido crear el articulo</h3>")
