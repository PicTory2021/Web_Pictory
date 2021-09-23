from django.shortcuts import render
from .models import pictory_test
def index(request):
	# 경로 지정에 templates 하위 경로를 지정해주면 된다.
    return render(request, 'appRS/index.html')

# def post_view(request):
#     posts = pictory_test.objects.all()
#     return render(request, '')