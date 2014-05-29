from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from article.models import Article
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.conf import settings
from haystack.query import SearchQuerySet

#from whoosh.index import open_dir
#from whoosh.qparser import QueryParse

from django.utils import timezone

import logging

logr = logging.getLogger(__name__)

# Create your views here.
def search_titles(request):
    '''
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Article.objects.filter(title__contains=search_text)
    '''
    articles = SearchQuerySet().autocomplete(conteent_auto=request.POST.get('search_text',''))
    return render_to_response('ajax_search.html',{'articles':articles})
    '''
    ix = open_dir(settings.WHOOSH_INDEX)

    articles = []
    
    if request.method == "POST":
        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            logr.debug(ix.schema)
            parser = QueryParser("body", schema=ix.schema)

            try:
                qry = parser.parse(search_text)
            except:
                qry = None

            if qry is not None:
                searcher = ix.searcher()
                articles = searcher.search(qry, terms=True)
                logr.debug(articles)

    return render_to_response('ajax_search.html',{'articles':articles})
    ''' 
    
def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/articles/get/%s' %article_id)

def create(request):
  if request.POST:
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()

      return HttpResponseRedirect('/articles/all')
  else:
    form = ArticleForm()

  args = {}
  args.update(csrf(request))

  args['form'] = form

  return render_to_response('create_article.html',args)

def articles(request):
  language = 'en-us'
  session_language = 'en-us'
  
  if 'lang' in request.COOKIES:
    language = request.COOKIES['lang']

  if 'lang' in request.session:
    session_language = request.session['lang']

  args = {}
  args.update(csrf(request))

  args['articles'] = Article.objects.all()
  args['languages'] = language
  args['session_language'] = session_language

  return render_to_response('articles.html',args)

def article(request, article_id=1):
    return render_to_response('article.html',
        {'article': Article.objects.get(id=article_id)})

def language(request,language='en-us'):
  response = HttpResponse("setting language to %s"%language)
  response.set_cookie('lang',language)
  request.session['lang'] = language
  return response

def hello(request):
  name = "Damon"
  html = "<html><body>Hi %s, this seems to have worked!</body></html>" %name
  return HttpResponse(html)

def hello_template(request):
  name="Damon"
  t = get_template('hello.html')
  html = t.render(Context({'name': name}))
  return HttpResponse(html)

class HelloTemplate(TemplateView):
  template_name='hello_class.html'

  def get_context_data(self, **kwargs):
    context = super(HelloTemplate,self).get_context_data(**kwargs)
    context['name'] = 'Damon'
    return context

