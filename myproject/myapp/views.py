from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.db.models import Q
from django.shortcuts import render_to_response, HttpResponseRedirect
from datetime import *
from forms import *
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from forms import *
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.paginator import *
import xlrd
from django.core import serializers
# from django.utils import simplejson as json
from django.core.serializers.json import DjangoJSONEncoder
from myapp import *
from django.template.loader import render_to_string
import datetime
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import hashlib
import random
from django.db import connection
from datetime import datetime, timedelta, date
from django.conf import settings as conf_settings
import os
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.mail import send_mail,  EmailMultiAlternatives
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
import datetime

def Login(request):
	# form = UserForm(request.POST)
	content = {}
	# content['form'] = form
	content.update(csrf(request))
	# if 'user' in request.session.keys():
	# 	return HttpResponseRedirect("/dashboard")
	if request.method == "POST":
		username = request.POST['userid']
		password = request.POST['password']
		print username
		user_list = members.objects.filter(user_id=username, password=password)
		if(user_list):
			userobj = user_list[0]   
			request.session['user'] = userobj
			return HttpResponseRedirect("/dashboard")
		else:
			content['err_msg'] = 'Invalid username or password'
		return render_to_response('login.html', content, context_instance=RequestContext(request))

	return render_to_response('login.html', content, context_instance=RequestContext(request))
def Logout(request):
	content = {}
	return render_to_response('login.html', content, context_instance=RequestContext(request))
def DashBoard(request):
	content = {}
	return render_to_response('index.html', content, context_instance=RequestContext(request))
# class Myview(View):
# 	def get(self,request):
# 		return HttpResponse("this is my view")
# 	def post(self,request):
# 		return HttpResponse("This is post method")
