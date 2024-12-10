from django.shortcuts import render


def hello(request):
    tags = ['Hero', 'I love you', 'Congratulation']
    rating = 3
    return render(request, 'index.html',
                  {'name':'Music In My Mind',
                   'Owner':'my mind',
                   'tags':tags,
                   'rating':rating
                   })
def home(request):
    return render(request, 'index.html')
#Views    
def waterfallvp(request):
    return render(request, 'page/views/park/waterfall.html')
def forestvp(request):
    return render(request, 'page/views/park/forest.html')
def mountainvp(request):
    return render(request, 'page/views/park/mountain.html')
def views(request):
    return render(request, 'page/views.html')
def naturev(request):
    return render(request, 'page/views/nature.html')
def parkv(request):
    return render(request, 'page/views/park.html')
def waterfallvp(request):
    return render(request, 'page/views/park/waterfall.html')
def forestvp(request):
    return render(request, 'page/views/park/forest.html')
def mountainvp(request):
    return render(request, 'page/views/park/mountain.html')
def waterfallvn(request):
    return render(request, 'page/views/nature/waterfall.html')
def forestvn(request):
    return render(request, 'page/views/nature/forest.html')
def mountainvn(request):
    return render(request, 'page/views/nature/mountain.html')

#travel  
def travel(request):
    return render(request, 'page/travel.html')  
def naturea(request):
    return render(request, 'page/travel/nature.html')
def parka(request):
    return render(request, 'page/travel/park.html')
def waterfallap(request):
    return render(request, 'page/travel/park/waterfall.html')
def forestap(request):
    return render(request, 'page/travel/park/forest.html')
def mountainap(request):
    return render(request, 'page/travel/park/mountain.html')
def waterfallan(request):
    return render(request, 'page/travel/nature/waterfall.html')
def forestan(request):
    return render(request, 'page/travel/nature/forest.html')
def mountainan(request):
    return render(request, 'page/travel/nature/mountain.html')
def seaan(request):
    return render(request, 'page/travel/nature/sea.html')
def seavp(request):
    return render(request, 'page/travel/park/sea.html')