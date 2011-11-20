# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):

    return render_to_response('index/index.html')

def busca(request):

    return render_to_response('index/busca.html')
