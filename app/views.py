from django.shortcuts import render
from .models import product
from .documents import ProductDocument
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from elasticsearch_dsl.query import Q

@csrf_exempt
def home(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        data = ProductDocument.search().query(Q("match",name=name) | Q("match",description=name))
        data= data.to_queryset().values()
        return JsonResponse(list(data),safe=False)

    data = ProductDocument.search().query(Q("match_phrase",name="madaa") | Q("match",description="eye"))
    # print("########",data)
    return render(request,"app/articles.html",{"product":data})
