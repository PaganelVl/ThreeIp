from django.shortcuts import render
from django.template.response import TemplateResponse
from django import forms
from ip2geotools.databases.noncommercial import DbIpCity


class Form():
    ip = forms.CharField(label='Type IP')


def index(request):
    userform = Form()
    data = {"form": userform}

    return render(request, 'index.html', data)


def result(request):
    ip = str(request.POST.get('ip'))

    data = DbIpCity.get(ip)

    data = {
        'ip': ip,
        'city': data.city,
        'region': data.region,
        'country': data.country,
        'latitude': data.latitude,
        'longitude': data.longitude,
    }

    return TemplateResponse(request, 'result.html', data)
