from django.shortcuts import render, redirect
from .models import Page
from markdown import markdown


def index(req):
    pages = Page.objects.order_by("id")[::-1]
    print(pages)
    context = {
        "mkpages": [{"mkpage": markdown(page.markdown_field, extensions=['fenced_code', 'codehilite']), 
                    "title": page.title, 
                    "id": page.id
                    } for page in pages]
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

def delete(req, id):
    page = Page.objects.filter(id=id)[0]
    page.delete()
    return redirect('index')