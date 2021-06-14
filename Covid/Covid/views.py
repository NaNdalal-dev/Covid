from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound

error404 = lambda request,exception : render(request,'404.html')
