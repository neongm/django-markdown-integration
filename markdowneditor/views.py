from django.shortcuts import render, redirect
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
    if req.method == "POST":
        title = req.POST.get("title")
        mkfield = req.POST.get("mkfield")
        page = Page(title=title, markdown_field=mkfield)
        page.save()
        return redirect('index')
    return render(req, 'markdowneditor/editor.html')