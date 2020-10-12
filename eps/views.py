from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import *


# Create your views here.
def start(request):
    return render(request, 'eps/start-page1.html', {})


def fiz(request):
    unsortedlist = []
    for i in range(2, len(Bank_ind.objects.all())):
        a = (0.2 * float(Bank_ind.objects.get(id=i).security) + 0.5 *
             float(Bank_ind.objects.get(id=i).CrCardExist) + 0.7 *
             float(Bank_ind.objects.get(id=i).DebCardExist) + 0.3 *
             float(Bank_ind.objects.get(id=i).PremCardExist) + 0.15 *
             float(Bank_ind.objects.get(id=i).RubDep) + 0.3 *
             float(Bank_ind.objects.get(id=i).DolDep) + 2 *
             float(Bank_ind.objects.get(id=i).EurDep) + 0.1 *
             float(Bank_ind.objects.get(id=i).MultivDepExist) + 3.5 / float(
                    Bank_ind.objects.get(id=i).CrRealEstate) + 9.6 /
             float(Bank_ind.objects.get(id=i).CrWtLoan) + 4 / float(Bank_ind.objects.get(id=i).CrRealEstateAuto) + 0.2 *
             float(Bank_ind.objects.get(id=i).Refinancing) + 0.5 / float(Bank_ind.objects.get(id=i).AutoCr) +
             0.6 * float(Bank_ind.objects.get(id=i).Deposits) + 0.4 * float(
                    Bank_ind.objects.get(id=i).Insurance) + 0.3 *
             float(Bank_ind.objects.get(id=i).Investments) + 0.3 * float(Bank_ind.objects.get(id=i).MobApp) + 0.1 *
             float(Bank_ind.objects.get(id=i).MobConn)
             )
        genunsortedlist = unsortedlist.append(a)  # TODO: sorting
    return render(request, 'eps/fiz1.html', {})


def yur(request):
    return render(request, 'eps/yur1.html', {})


def corp(request):
    return render(request, 'eps/corp1.html', {})


def result(request):
    return render(request, 'eps/dbo-list1.html', {})

# class Start(TemplateView):
# template_name = "eps/start-page.html"


# class Fiz(TemplateView):
# template_name = "eps/fiz.html"


# class Yur(TemplateView):
# template_name = "eps/yur.html"


# class Corp(TemplateView):
# template_name = "eps/corp.html"
