import json
import random

from django.shortcuts import render
from .models import Image, UserDB, DetailClick, goodBad
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.conf import settings
from django.db.models import Q
from .clustering import init_select_img, select_img, recommendation
from django.db import connection
import json
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt

def index(request):
    randImage = Image.objects.all().order_by("?")[0:6]
    for i in randImage:
        if(len(i.Contents)>250):
            i.Contents = i.Contents[0:250]
            i.Contents +="..."
    for i in randImage:
        i.Name = i.Name.replace('"','').replace('"','')
        i.Url = "/static/tour_img/%s1%s" % (i.Name, i.Extension)
    context = {'randImage': randImage}

    return render(request, 'appRS/index.html', context)
@csrf_exempt
def main(request):
    if request.method =='POST':
        # 선택 후, 추천 알고리즘 결과 사진 전송
        print("main")
        data = json.loads(request.body)
        selected = data['selected']
        userId = int(data['userId'])

        if len(data['selected']) == 3:
            # rec_id = Image.objects.all().order_by("?").only('Id')[0:3]  # id 값만 가져오기(임시)
            # rec_json = serializers.serialize('json',rec_id)

            gb = goodBad(userId=userId, select1=selected[0], select2=selected[1], select3=selected[2],
                         rec1='', rec2='', rec3='', eval=None)
            gb.save()
            context = {'url': 'result'}
            return JsonResponse(context, content_type="application/json")

        else :
            for i in range(0,len(selected)):
                selected[i] = int(selected[i])
            rec_id = select_img(selected)
            randImage = Image.objects.filter(Q(Id=rec_id[0]) | Q(Id=rec_id[1]) | Q(Id=rec_id[2]) | Q(Id=rec_id[3]) | Q(Id=rec_id[4]) | Q(Id=rec_id[5]))
            for i in randImage:  #name의 큰따옴표 없애주기
                i.Name = i.Name.replace('"', '').replace('"', '')
            randImage = serializers.serialize('json', randImage)
            context = {'randImage': randImage}
            return JsonResponse(context, content_type="application/json")

    else:
        # 처음 사진 선택 시, 보여지는 사진 전송
        rec_id = init_select_img()
        randImage = Image.objects.filter(Q(Id=rec_id[0]) | Q(Id=rec_id[1]) | Q(Id=rec_id[2]) | Q(Id=rec_id[3]) | Q(Id=rec_id[4]) | Q(Id=rec_id[5]))
        for i in randImage:
            i.Name = i.Name.replace('"', '').replace('"', '')
            i.Url = "/static/tour_img/%s1%s" % (i.Name, i.Extension)
        context = {'randImage': randImage}
        return render(request, 'appRS/main.html', context)

@csrf_exempt
def result(request, id):
    selected=[]
    rec_id=[]
    userId = id

    # 같은 userId 를 가진 레코드가져오기
    qs = goodBad.objects.filter(userId=userId)
    # 그 중, 마지막 레코드 가져오기
    sp = qs[len(qs)-1]
    selected.append(int(sp.select1))
    selected.append(int(sp.select2))
    selected.append(int(sp.select3))
    if sp.rec1 == '':
        # 추천결과 3장 id 값 가져오기
        rec_id = recommendation(selected)
        # rec 1,2,3 update
        sp.rec1 = rec_id[0]
        sp.rec2 = rec_id[1]
        sp.rec3 = rec_id[2]
        # 저장
        sp.save()
    else :
        rec_id.append(int(sp.rec1))
        rec_id.append(int(sp.rec2))
        rec_id.append(int(sp.rec3))

    recImage = Image.objects.filter(Q(Id=rec_id[0]) | Q(Id=rec_id[1]) | Q(Id=rec_id[2]))
    for i in recImage:
        i.Name = i.Name.replace('"', '').replace('"', '')
        i.Url = "/static/tour_img/%s1%s" % (i.Name, i.Extension)

    context = {'recImage': recImage}
    return render(request, 'appRS/result.html', context)

@csrf_exempt
def nearLocation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Lat = data['Latitude'] # 위도
        Lon = data['Longitude'] # 경도
        if Lat != "" and Lon != "" :
            # Lat = 35.1171597
            # Lon = 128.9676741
            print(type(Lon))
            # conn = pymysql.connect(host='localhost',
            #                        user='yeon', password='now0913', db='pictory', charset='utf8')
            try:
                cursor = connection.cursor()

                sql = "SELECT *,(6371*acos(cos(radians({Lat}))*cos(radians(Latitude))*cos(radians(Longitude)-radians({Lon}))" \
                      "+sin(radians({Lat}))*sin(radians(Latitude))))" \
                      "AS distance FROM apprs_image HAVING distance <= 5 ORDER BY distance LIMIT 50".format(Lat=Lat, Lon=Lon)
                print(sql)
                cursor.execute(sql)
                print("excute")
                rows = cursor.fetchall()
                print("fetchall")
                nearImages=[]
                random_i = []
                ran_num = random.randint(0,len(rows)-1)
                for i in range(6):
                    while ran_num in random_i:
                        ran_num = random.randint(0,len(rows)-1)
                    random_i.append(ran_num)

                for i in random_i:
                    row = {'Id':rows[i][0],
                           'Name':rows[i][1].replace('"', '').replace('"', ''),
                           'Extension':rows[i][2],
                           'ZipCode':rows[i][3],
                           'Address':rows[i][4],
                           'Contents':rows[i][5],
                           'Latitude':rows[i][6],
                           'Longitude':rows[i][7],
                           'Url': "/static/tour_img/%s1%s" % (rows[i][1], rows[i][2])
                           }
                    nearImages.append(row)
                for i in nearImages:
                    if (len(i['Contents']) > 200):
                        i['Contents'] = i['Contents'][0:200]
                        i['Contents'] += "..."
                # for i in nearImages:
                #     i[1] = i[1].replace('"', '').replace('"', '')
                #     i[7] = "/static/tour_img/%s1%s" % (i[1], i[7])
                # nearImages = serializers.serialize('json', nearImages)
                print(1)
                context = {'randImage': nearImages}
                print(context)
                print(2)
                # print(type(context))
                # print(nearImages)
                # connection.commit()
                connection.close()

            except Exception as e:
                connection.rollback()
                context = {'randImage': 'fail'}
                print("Failed selecting  ", e)
                return Http404()
            return JsonResponse(context, content_type="application/json")
        else:
            return Http404()

@csrf_exempt
def getContext(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data['id']
        get_context = Image.objects.filter(Id=id)
        get_context = serializers.serialize('json',get_context)
        context={"context" : get_context}
        return JsonResponse(context, content_type="application/json")

@csrf_exempt
def eval(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        eval = data['eval']
        userId = data['userId']
        qs = goodBad.objects.filter(userId=userId)
        sp = qs[len(qs) - 1]
        sp.eval = eval
        sp.save()
        return HttpResponse(request,'appRS/result.html')


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