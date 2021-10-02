import json

from django.shortcuts import render
from .models import Image, UserDB, DetailClick
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.conf import settings


selected_images=[]

@csrf_exempt
def index(request):
    randImage = Image.objects.all().order_by("?")[0:6]
    # for i in randImage:
    #     if(len(i.Contents)>250):
    #         i.Contents = i.Contents[0:250]
    #         i.Contents +="..."
    context = {'randImage': randImage }

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
    randImage = Image.objects.all().order_by("?")[0:3]
    context = {'randImage': randImage}
    return render(request, 'appRS/result.html', context)

@csrf_exempt
def test(request):
    randImage = Image.objects.all().order_by("?")[0:6]
    context = {'randImage': randImage}
    return render(request, 'appRS/test.html', context)

@csrf_exempt
def get_user(request):
    if request.method == 'POST':
        UserId = len(UserDB.objects.all()) + 1
        UserName = json.loads(request.body)
        user = UserDB(UserId=UserId, UserName=UserName)
        user.save()

        json_data = json.dumps({'userid': UserId, 'username': UserName})
        jsonUser = {'jsonUser': json_data}
        return JsonResponse(jsonUser, content_type="application/json")

@csrf_exempt
def detailClick(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        savedb = DetailClick(UserId=data['UserId'], UserName=data['UserName'], SelectImage=data['SelectImage'],
                             clickOpenDate=data['clickOpenDate'], stayTime=data['stayTime'])
        print(savedb)
        savedb.save()

    return JsonResponse(data, content_type="application/json")