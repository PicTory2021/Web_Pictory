from django.shortcuts import render
from .models import Image
from django.conf import settings


def index(request):

    randImage = Image.objects.all().order_by("?")[0:6]
    # for i in randImage:
    #     if(len(i.Contents)>250):
    #         i.Contents = i.Contents[0:250]
    #         i.Contents +="..."
    context = {'randImage': randImage,
               'mapApiKey':settings.KAKAO_MAPS_API_KEY,
               'test':"TEST"
               }
    print(context['test'])

    return render(request, 'appRS/index.html', context)


