from django.shortcuts import render
from.models import post


def one(request):
	obj =post.objects.all()
	context={'model':obj}
	return render(request,'portfolio/home.html',context)
