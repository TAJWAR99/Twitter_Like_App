import random
from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,'pages/home.html',context={},status=200)

def tweet_create_view(request,*args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()
    return render(request,'components/form.html',{"form":form})

def tweet_list_view(request,*args, **kwargs):
    '''REST API VIEW'''
    qs = Tweet.objects.all()
    tweets_list = [{'id':x.id,'content':x.content,'likes':random.randint(0,56)} for x in qs]
    data = {
        'isUser': False,
        'response': tweets_list
    }
    return JsonResponse(data)
    # return JsonResponse({tweets_list})

def tweet_detail_view(request,tweet_id,*args, **kwargs):
    '''REST API VIEW'''
    data = {
        "id":tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    
    return JsonResponse(data,status=status)
