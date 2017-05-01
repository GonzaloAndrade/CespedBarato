# coding: utf8
from django.http import HttpResponse
from django.template import Context, loader
from django import forms
from django.shortcuts import render_to_response
from django.core.mail import send_mail
import datetime
import json


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def index():
    template = loader.get_template("home/index.html")
    return HttpResponse(template.render())


def contact(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            textarea = request.POST.get('textarea')

            select = request.POST.get('select')

            text = "Usuario: "+name +" Telefono: " +phone+ " Mensaje: " + textarea
            response_data = name

            # Enviar correo
            send_mail(select, text, email, ['info@cespedbarato.ec'],
                      fail_silently=False)
            return HttpResponse(json.dumps("success"), content_type="application/json")
