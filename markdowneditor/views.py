from django.shortcuts import render, redirect
from .models import Page
from markdown import markdown
from random import randint
import math

def index(req, page_id=0):
    id_error_message = "This place is dark and empty. Too empty."
    if(page_id==randint(0, 1000)):
        page_id=99999999
        id_error_message="Wow. That's an impressive accident."

    content_per_page = 10
    pages = Page.objects.order_by("id")[::-1]
    all_pages_numbers = [page_number for page_number in range(0, math.ceil(len(pages)/content_per_page))]
    amount_of_pages = len(all_pages_numbers)

    print("  ", amount_of_pages, len(Page.objects.order_by("id")))

    current_page_id = page_id
    next_page_link = page_id+1 if page_id < amount_of_pages else None
    prev_page_link = page_id-1 if page_id > 0 else None
    mkpages = [{"mkpage": markdown(page.markdown_field, extensions=['fenced_code', 'codehilite']),
                    "title": page.title,
                    "id": page.id
                    } for page in pages [page_id*content_per_page : (page_id+1)*content_per_page :] ]

    if(page_id==6969): id_error_message = "Ha-ha, nice, but no."


    context = {
        "mkpages": mkpages,
        "all_pages_links" : all_pages_numbers,
        "current_page_id": current_page_id,
        "next_page_link" : next_page_link,
        "prev_page_link" : prev_page_link,
        "id_error_message": id_error_message
    }
    print(context["all_pages_links"],
          context["next_page_link"],
          context["prev_page_link"])
    return render(req, 'index/index.html', context)


def editor(req):
    if req.method == "POST":
        title = req.POST.get("title")
        mkfield = req.POST.get("mkfield")
        page = Page(title=title, markdown_field=mkfield)
        page.save()
        return redirect('index_start')
    return render(req, 'markdowneditor/editor.html')

def delete(req, id):
    try:
        page = Page.objects.filter(id=id)[0]
        page.delete()
    except: pass
    return redirect('index_start')