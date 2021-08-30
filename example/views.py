from django.contrib.postgres import search
from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery,SearchVector,SearchRank,SearchHeadline
# Create your views here.
from .models import User, Video

def Home(request):
    text = request.GET.get('search_text')
    # text = None
    if text:
        vector = SearchVector('fname','email')
        query = SearchQuery(text)
        print(vector)
        # data = User.objects.annotate(search=vector).filter(search=query)
        data = User.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gte=0.001).order_by('-rank')

        print(data)
    else:
        data = None
    context = {
        'data':data
    }
    return render(request,'example/index.html',context)