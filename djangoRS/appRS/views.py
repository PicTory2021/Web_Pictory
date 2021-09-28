import json

from django.shortcuts import render
from .models import Image
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

selected_images=[]

@csrf_exempt
def index(request):
    randImage = Image.objects.all().order_by("?")[0:6]
    for i in randImage:
        if(len(i.Contents)>250):
            i.Contents = i.Contents[0:250]
            i.Contents +="..."
    context = {'randImage': randImage}

    return render(request, 'appRS/index.html', context)

@csrf_exempt
def main(request):
    if request.method =='POST':
        # 선택 후, 추천 알고리즘 결과 사진 전송
        data = json.loads(request.body)
        print(data)
        randImage = serializers.serialize("json",Image.objects.all().order_by("?")[0:6])
        context = {'randImage': randImage}
        return JsonResponse(context, content_type="application/json")

    else:
        # 처음 사진 선택 시, 보여지는 사진 전송
        randImage = Image.objects.all().order_by("?")[0:6]
        context = {'randImage': randImage}
        return render(request, 'appRS/main.html', context)

@csrf_exempt
def result(request):
    return render(request, 'appRS/result.html')