from django.shortcuts import render

from .models import Page
#from django.http import HttpResponse

def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title' : pg.title,
        'content' : pg.bodytext,
        'last_updated':pg.update_date,
        'page_list':Page.objects.all(),
    }
    #assert False
    return render(request,'pages/page.html', context)

# Create your views here.
