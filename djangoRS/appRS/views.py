from django.shortcuts import render
from .models import Image


def index(request):
    randImage = Image.objects.all().order_by("?")[0:6]
    for i in randImage:
        if(len(i.Contents)>250):
            i.Contents = i.Contents[0:250]
            i.Contents +="..."
    context = {'randImage': randImage}

    return render(request, 'appRS/index.html', context)


def main(request):
    if request.method =='POST':
        # 선택 후, 추천 알고리즘 결과 사진 전송
        print(request.POST.get('select1'))
        randImage = Image.objects.all().order_by("?")[0:6]
        context = {'randImage': randImage}
        return render(request, 'appRS/main.html',context)
    else:
        # 처음 사진 선택 시, 보여지는 사진 전송
        randImage = Image.objects.all().order_by("?")[0:6]
        context = {'randImage': randImage}
        return render(request, 'appRS/main.html', context)


