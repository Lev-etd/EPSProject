from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .models import *
from .forms import *


# Create your views here.
def start(request):
    return render(request, 'eps/start-page1.html', {})


def fiz(request):
    fizrad = FizRadio()
    multcheck = MultCheckCrit()
    bankcard = BankCard()
    depositRub = DepositRadioRub()
    depositDol = DepositRadioDol()
    depositEur = DepositRadioEur()
    credit = CredRadio()
    creditwh = CredWHRadio()
    creditwpledge = CredWPledgeRadio()
    autocr = AutoCrRadio()

    context = {'fizrad': fizrad, 'multcheck': multcheck, 'bankcard': bankcard, 'depositrub': depositRub,
               'depositdol': depositDol, 'depositEur': depositEur, "credit": credit,
               "creditwh": creditwh, "creditwpledge": creditwpledge, "autocr": autocr}

    return render(request, 'eps/fiz1.html', context)


def yur(request):
    fizrad = FizRadio()
    bankfunc = BankFuncYur()
    revcr = RevCred()
    credline = CredLine()
    credrevline = RevCredLine()
    investline = InvestCredLine()
    credip = CredIP()
    credipprop = CredIPProp()
    context = {'fizrad': fizrad, 'bankfunc': bankfunc, 'revcr': revcr, 'credline': credline, 'credrevline': credrevline,
               'investline': investline, 'credip': credip, 'credipprop': credipprop, }

    return render(request, 'eps/yur1.html', context)


def corp(request):
    fizrad = FizRadio()
    bfuncyur = BankFuncCorp()
    context = {"fizrad": fizrad, "bfuncyur": bfuncyur}
    return render(request, "eps/corp1.html", context)


def resultfiz(request):
    if request.method == 'POST':
        fizradform = FizRadio(request.POST)
        multcheckform = MultCheckCrit(request.POST)
        bankcardform = BankCard(request.POST)
        depositRub = DepositRadioRub(request.POST)
        depositDol = DepositRadioDol(request.POST)
        depositEur = DepositRadioEur(request.POST)
        credit = CredRadio(request.POST)
        creditwh = CredWHRadio(request.POST)
        creditwpledge = CredWPledgeRadio(request.POST)
        autocr = AutoCrRadio(request.POST)
        if (autocr.is_valid() and depositRub.is_valid()
                and depositDol.is_valid() and fizradform.is_valid() and credit.is_valid() and creditwh.is_valid()
                and creditwpledge.is_valid() and depositEur.is_valid() or (
                        multcheckform.is_valid() and bankcardform.is_valid())):

            unsortedlist = []
            multlistbig = []
            multlistsmall = []
            if not multcheckform.is_valid():
                multlistbig = [0, 0, 0, 0, 0, 0, 0]
            else:
                for i in ["refinance", "deposits", "insurance", "investments", "mobapp", "mobconn", "multi"]:
                    if i in multcheckform.cleaned_data["multcheckform"]:
                        multlistbig.append(1)
                    else:
                        multlistbig.append(0)

            if not bankcardform.is_valid():
                multlistsmall = [0, 0, 0, 0, 0, 0, 0]
            else:
                for i in ["credit", "debet", "prem"]:
                    if i in bankcardform.cleaned_data["bkcr"]:
                        multlistsmall.append(1)
                    else:
                        multlistsmall.append(0)

            for i in range(2, len(Bank_ind.objects.all())):
                unsortedlist.append(round(
                    fizradform.cleaned_data["ten_form"] * 0.2 * float(Bank_ind.objects.get(id=i).security) +
                    0.5 * multlistsmall[0] *
                    float(Bank_ind.objects.get(id=i).CrCardExist) + 0.7 * multlistsmall[1] *
                    float(Bank_ind.objects.get(id=i).DebCardExist) + 0.3 * multlistsmall[2] *
                    float(Bank_ind.objects.get(id=i).PremCardExist) + 0.15 * depositRub.cleaned_data["depradr"] *
                    float(Bank_ind.objects.get(id=i).RubDep) + 0.3 * depositDol.cleaned_data["depradd"] *
                    float(Bank_ind.objects.get(id=i).DolDep) + 2 * depositEur.cleaned_data["deprade"] *
                    float(Bank_ind.objects.get(id=i).EurDep) + 0.1 * multlistbig[6] *
                    float(Bank_ind.objects.get(id=i).MultivDepExist) + credit.cleaned_data["credrad"] * (3.5 / float(
                        Bank_ind.objects.get(id=i).CrRealEstate)) + creditwh.cleaned_data["cwhc"] * (9.6 /
                                                                                                     float(
                                                                                                         Bank_ind.objects.get(
                                                                                                             id=i).CrWtLoan)) +
                    creditwpledge.cleaned_data["cwpr"] * (4 / float(
                        Bank_ind.objects.get(id=i).CrRealEstateAuto)) + 0.2 * multlistbig[0] *
                    float(Bank_ind.objects.get(id=i).Refinancing) + autocr.cleaned_data["acr"] * 0.5 / float(
                        Bank_ind.objects.get(id=i).AutoCr) +
                    0.6 * multlistbig[1] * float(Bank_ind.objects.get(id=i).Deposits) + 0.4 * multlistbig[2] * float(
                        Bank_ind.objects.get(id=i).Insurance) + 0.3 * multlistbig[3] *
                    float(Bank_ind.objects.get(id=i).Investments) + 0.3 * multlistbig[4] * float(
                        Bank_ind.objects.get(id=i).MobApp) + 0.1 * multlistbig[5] *
                    float(Bank_ind.objects.get(id=i).MobConn)
                    , 2))

            unsorteddict = {}
            for i in range(2, len(Bank_ind.objects.all())):
                for j in unsortedlist:
                    unsorteddict[Bank_ind.objects.get(id=i).name] = j
                    unsortedlist.remove(j)
                    break
            sortedlist = sorted(unsorteddict, key=unsorteddict.get, reverse=True)

            return render(request, 'eps/dbo-list1.html', {"a": sortedlist})
    else:
        fizradform = FizRadio()
        multcheckform = MultCheckCrit()
        bankcardform = BankCard()
        depositRub = DepositRadioRub()
        depositDol = DepositRadioDol()
        depositEur = DepositRadioEur()
        credit = CredRadio()
        creditwh = CredWHRadio()
        creditwpledge = CredWPledgeRadio()
        autocr = AutoCrRadio()

    return render(request, 'eps/dbo-list1.html', {'a': "WRONG"})


def resultyur(request):
    if request.method == 'POST':
        fizrad = FizRadio(request.POST)
        bankfunc = BankFuncYur(request.POST)
        revcr = RevCred(request.POST)
        credline = CredLine(request.POST)
        credrevline = RevCredLine(request.POST)
        investline = InvestCredLine(request.POST)
        credip = CredIP(request.POST)
        credipprop = CredIPProp(request.POST)

        if (fizrad.is_valid() and revcr.is_valid() and credline.is_valid()
                and credrevline.is_valid() and investline.is_valid() and credip.is_valid() and credipprop.is_valid() or bankfunc.is_valid()):
            unsortedlistyur = []
            multlistyur = []

            if not bankfunc.is_valid():
                multlistyur = [0, 0, 0, 0, 0, 0, 0]
            else:
                for i in ["account", "overdraft", "deposits", "MobBack"]:
                    if i in bankfunc.cleaned_data["bfy"]:
                        multlistyur.append(1)
                    else:
                        multlistyur.append(0)

            for i in range(2, len(Bank_ind.objects.all())):
                unsortedlistyur.append(round(
                    fizrad.cleaned_data["ten_form"] * 0.2 * float(Bank_legal.objects.get(id=i).Security) +
                    0.4 * multlistyur[3] *
                    float(Bank_legal.objects.get(id=i).MobBank) + 0.7 * multlistyur[2] *
                    float(Bank_legal.objects.get(id=i).Deposits) + 0.3 * multlistyur[1] *
                    float(Bank_legal.objects.get(id=i).Overdraft) + credip.cleaned_data["crep"] * (4 / float(
                        Bank_legal.objects.get(id=i).AnyCreditEstate)) + credipprop.cleaned_data["cripp"] * (8 /
                                                                                                             float(
                                                                                                                 Bank_legal.objects.get(
                                                                                                                     id=i).AnyCredit)) +
                    investline.cleaned_data["invecstcl"] * (8 /
                                                            float(Bank_legal.objects.get(id=i).InvestCreditLine)) +
                    credrevline.cleaned_data["rcl"] * (4 /
                                                       -(float(Bank_legal.objects.get(id=i).RevCreditLine))) +
                    credline.cleaned_data["cl"] * (10.4 /
                                                   float(Bank_legal.objects.get(id=i).CreditLine)) + revcr.cleaned_data[
                        "rc"] * (10.4 /
                                 float(Bank_legal.objects.get(id=i).RevCreditLine)) + 1 * multlistyur[0] * float(
                        Bank_legal.objects.get(id=i).opening)
                    , 2))

            unsorteddict = {}
            for i in range(1, len(Bank_legal.objects.all())):
                for j in unsortedlistyur:
                    unsorteddict[Bank_legal.objects.get(id=i).name] = j
                    unsortedlistyur.remove(j)
                    break
            sortedlist = sorted(unsorteddict, key=unsorteddict.get, reverse=True)

            return render(request, 'eps/dbo-list1.html', {"a": sortedlist})
    else:
        fizrad = FizRadio()
        bankfunc = BankFuncYur()
        revcr = RevCred()
        credline = CredLine()
        credrevline = RevCredLine()
        investline = InvestCredLine()
        credip = CredIP()
        credipprop = CredIPProp()

    return render(request, 'eps/dbo-list1.html', {'a': "WRONG"})


def resultcorp(request):
    if request.method == 'POST':
        fizradform = FizRadio(request.POST)
        bankfuncform = BankFuncCorp(request.POST)
        if fizradform.is_valid() or bankfuncform.is_valid():
            unsortedlistcorp = []
            multcorp = []

            if not bankfuncform.is_valid():
                multcorp = [0, 0, 0, 0, 0, 0, 0]
            else:
                for i in ["account", "overdraft", "expcred", "intavail", "salprojavail", "deposits", "intappavail"]:
                    if i in bankfuncform.cleaned_data["bfcp"]:
                        multcorp.append(1)
                    else:
                        multcorp.append(0)

            for i in range(1, len(Bank_ind.objects.all())):
                unsortedlistcorp.append(round(
                    fizradform.cleaned_data["ten_form"] * 0.3 * float(Bank_corp.objects.get(id=i).Security) +
                    1.5 * float(Bank_corp.objects.get(id=i).opening) * multcorp[0] +
                    1 * float(Bank_corp.objects.get(id=i).ExpCred) * multcorp[2] +
                    0.6 * float(Bank_corp.objects.get(id=i).Overdraft) * multcorp[1] +
                    0.7 * float(Bank_corp.objects.get(id=i).IntPlace) * multcorp[3] + 2 * float(
                        Bank_corp.objects.get(id=i).SalProj) * multcorp[4] +
                    0.5 * float(Bank_corp.objects.get(id=i).Deposits) * multcorp[5] + 0.7 * float(
                        Bank_corp.objects.get(id=i).WebApp) * multcorp[6], 2))


            unsorteddict = {}
            for i in range(1, len(Bank_corp.objects.all())):
                for j in unsortedlistcorp:
                    unsorteddict[Bank_corp.objects.get(id=i).name] = j
                    unsortedlistcorp.remove(j)
                    break
            sortedlist = sorted(unsorteddict, key=unsorteddict.get, reverse=True)
            return render(request, 'eps/dbo-list1.html', {"a": sortedlist})

    else:
        fizradform = FizRadio(request.POST)
        bankfuncform = BankFuncCorp(request.POST)

    return render(request, 'eps/dbo-list1.html', {'a': "WRONG"})


