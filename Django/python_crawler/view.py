from django.shortcuts import render
from django.http import HttpResponse
from crawler.models import Movies
from crawler.models import Weathers
from crawler.models import Phones
from django.db.models import Q

def index(request):
    context = {}
    context['hello']='欢迎'
    return render(request, 'index.html', {'hello':'欢迎'})

def login(request):
    return render(request, 'login.html')

def movies(request):
    movies=Movies.objects.all()
    return render(request, 'movies.html',{'movies': movies,'hello':'豆瓣TOP250部电影'})

def weathers(request):
    weathers=Weathers.objects.all()
    return render(request, 'weathers.html', {'weathers': weathers,'hello':'各地天气情况'})

def phones(request):
    phones=Phones.objects.all()
    return render(request, 'phones.html', {'phones': phones,'hello':'京东小米9'})
    

def searchmovies(request):
    context={}
    if request.POST:
        context['key']=request.POST['key']
    movies=Movies.objects.filter(Q(name__icontains=context['key'])|Q(synopsis__icontains=context['key'])|Q(time__icontains=context['key']))
    return render(request, 'movies.html', {'movies': movies,'searchkey':context['key']})

def searchphones(request):
    context={}
    if request.POST:
        context['key']=request.POST['key']
    phones=Phones.objects.filter(Q(name__icontains=context['key'])|Q(price__icontains=context['key'])|Q(time__icontains=context['key']))
    return render(request, 'phones.html', {'phones': phones,'searchkey':context['key']})

def searchweathers(request):
    context={}
    if request.POST:
        context['key']=request.POST['key']
    weathers=Weathers.objects.filter(Q(city__icontains=context['key'])|Q(dates__icontains=context['key'])|Q(winL__icontains=context['key'])
    |Q(temperatureLow__icontains=context['key'])|Q(temperatureHigh__icontains=context['key'])|Q(weather__icontains=context['key']))
    return render(request, 'weathers.html', {'weathers': weathers,'searchkey':context['key']})


    
