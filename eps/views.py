from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
# def start(request):
#     return render(request, 'eps/start-page.html', {})
#
#
# def fiz(request):
#     return render(request, 'eps/fiz.html', {})
#
#
# def yur(request):
#     return render(request, 'eps/yur.html', {})
#
#
# def corp(request):
#     return render(request, 'eps/corp.html', {})


class Start(TemplateView):
    template_name = "eps/start-page.html"


class Fiz(TemplateView):
    template_name = "eps/fiz.html"


class Yur(TemplateView):
    template_name = "eps/yur.html"


class Corp(TemplateView):
    template_name = "eps/corp.html"
