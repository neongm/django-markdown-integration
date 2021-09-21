from django.shortcuts import render
from .models import Page
from markdown import markdown


def index(req):

    pages = Page.objects.order_by("title")
    print(pages)
    context = {
        'mkpages': [{"mkpage": markdown(page.markdown_field), "title": page.title} for page in pages]
    }
    return render(req, 'index/index.html', context)


def editor(req):
    return render(req, 'markdowneditor/editor.html')