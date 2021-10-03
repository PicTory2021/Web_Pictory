import json

from django.shortcuts import render
from .models import Image, UserDB, DetailClick, goodBad
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.conf import settings
from django.db.models import Q


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
        print("main")
        data = json.loads(request.body)
        selected = data['selected']
        username = data['username']
        if len(data['selected']) == 3:
            print(selected)
            # rec_id = Image.objects.all().order_by("?").only('Id')[0:3]  # id 값만 가져오기(임시)
            # rec_json = serializers.serialize('json',rec_id)

            gb = goodBad(username=username, select1=selected[0], select2=selected[1], select3=selected[2],
                         rec1='', rec2='', rec3='', eval=None)
            gb.save()
            print("save")
            context = {'url': 'result', 'select3': selected[2]}
            return JsonResponse(context, content_type="application/json")

        else :
            print(selected)
            randImage = serializers.serialize("json",Image.objects.all().order_by("?")[0:6])
            context = {'randImage': randImage}
            return JsonResponse(context, content_type="application/json")

    else:
        # 처음 사진 선택 시, 보여지는 사진 전송
        randImage = Image.objects.all().order_by("?")[0:6]
        context = {'randImage': randImage}
        return render(request, 'appRS/main.html', context)

@csrf_exempt
def result(request, id):
    username = 'dfdd'
    sel3 = id
    print(sel3)
    rec_id = Image.objects.all().order_by("?").values('Id')[0:3]  # id 값만 가져오기(임시)
    recImage = Image.objects.filter(Q(Id=rec_id[0]['Id']) | Q(Id=rec_id[1]['Id']) | Q(Id=rec_id[2]['Id']))

    # 같은 userId 를 가진 레코드가져오기
    qs = goodBad.objects.filter(username=username)
    # 그 중, 마지막 레코드 가져오기
    sp = qs[len(qs)-1]
    # rec 1,2,3 update
    sp.rec1 = recImage[0].Id
    sp.rec2 = recImage[1].Id
    sp.rec3 = recImage[2].Id
    # 저장
    sp.save()
    context = {'recImage': recImage}
    return render(request, 'appRS/result.html', context)

@csrf_exempt
def eval(request):
    username = 'dfdd'
    if request.method == 'POST':
        data = json.loads(request.body)
        eval = data['eval']
        print(eval)
        qs = goodBad.objects.filter(username=username)
        sp = qs[len(qs) - 1]
        sp.eval = eval
        sp.save()
        return HttpResponse(request,'appRS/result.html')

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