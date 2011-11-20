# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response
from django.http import HttpResponse
from api.api import Twitter

def index(request):

    return render_to_response('index/index.html')

def busca(request):

    busca = request.REQUEST.get('busca')
    b = Twitter().getBusca(busca)
    request.session['resultados'] = b
    return render_to_response('index/busca.html', {"busca": b})

def gerar_xml(request):
    
    xml = "<?xml version='1.0' encoding='UTF-8'?>"
    xml = xml + '<principal>'
    xml = xml + '<resultados>'
    for res in request.session['resultados']: 
        xml = xml + "<resultado nome='"+res.from_user+"'>"+res.text+"</resultado>"
    xml = xml + '</resultados>'
    xml = xml + '</principal>'
    response = HttpResponse(mimetype='text/xml')
    response.write(xml)
    response['Content-Disposition'] = 'attachment; filename=unruly.xml'
    
    return response

