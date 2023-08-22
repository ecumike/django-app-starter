from django.shortcuts import render
from django.db.models import Count

from core.models import *

##
##	/
##
def home(request):
	context = {}
	
	return render(request, 'myapp/home.html', context)
	