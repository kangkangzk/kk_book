from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from test_blog.models import Sql

def article_content(request):
    article = Sql.objects.all()[0]
    title = article.title
    breief_content = article.brief_title
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title:%s,breief_content:%s,content:%s,article_id:%s,publish_date:%s' % \
                 (title, breief_content, content, article_id, publish_date)
    kk = return_str.encode()
    return HttpResponse(kk)

def get_index_page(request):
    all_aritle = Sql.objects.all()
    return render(request,'blog/index.html', {'article_list':all_aritle})
