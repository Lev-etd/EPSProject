from django import forms


class FizRadio(forms.Form):
    Choices = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8),
               (9, 9), (10, 10), ]

    ten_form = forms.IntegerField(
        widget=forms.RadioSelect(choices=Choices))


class MultCheckCrit(forms.Form):
    ChoicesCriteria = [("refinance", "Рефинансирование"), ("deposits", "Депозиты"), ("insurance", "Страхование"),
                       ("investments", "Инвестиции"),
                       ("mobapp", "Мобильное приложение"), ("mobconn", "Мобильная связь"),
                       ("multi", "Мультивалютный вклад")]

    multcheckform = forms.MultipleChoiceField(choices=ChoicesCriteria,
                                              widget=forms.CheckboxSelectMultiple)


class BankCard(forms.Form):
    cbc = [("credit", "Кредитные"), ("debet", "Дебетовые"), ("prem", "Премиальные")]

    bkcr = forms.MultipleChoiceField(choices=cbc,
                                     widget=forms.CheckboxSelectMultiple)


class DepositRadioRub(forms.Form):
    drr = [(4, "4%"), (5, "5%")]

    depradr = forms.IntegerField(
        widget=forms.RadioSelect(choices=drr))


class DepositRadioDol(forms.Form):
    drd = [(0, "0%"), (1, "0.1-0.3%"), (4, "0.4-0.6%"), ]

    depradd = forms.IntegerField(
        widget=forms.RadioSelect(choices=drd))


class DepositRadioEur(forms.Form):
    dre = [(0, "0%"), (1, "0.01%"), (11, "0.1%"), ]

    deprade = forms.IntegerField(
        widget=forms.RadioSelect(choices=dre))


class CredRadio(forms.Form):
    cc = [(7, "7-9%"), (11, "11-12%"), (15, "Более 15%")]

    credrad = forms.IntegerField(
        widget=forms.RadioSelect(choices=cc))


class CredWHRadio(forms.Form):
    cwc = [(6, "6-7%"), (8, "8-9%"), (10, "10-15%")]

    cwhc = forms.IntegerField(
        widget=forms.RadioSelect(choices=cwc))


class CredWPledgeRadio(forms.Form):
    crspr = [(8, "8-9%"), (10, "Более 10%")]

    cwpr = forms.IntegerField(
        widget=forms.RadioSelect(choices=crspr))


class AutoCrRadio(forms.Form):
    acrr = [(1, "1-2%"), (6, "6-9%"), (10, "Более 10%")]

    acr = forms.IntegerField(
        widget=forms.RadioSelect(choices=acrr))


class BankFuncYur(forms.Form):
    bfyu = [("account", "Открытие и обслуживание счета"), ("overdraft", "Овердрафт"), ("deposits", "Депозиты"),
            ("MobBack", "Наличие мобильного банка")]

    bfy = forms.MultipleChoiceField(choices=bfyu,
                                    widget=forms.CheckboxSelectMultiple)


class RevCred(forms.Form):
    revc = [(8, "8-10%"), (11, "11-13%"), (14, "14-15%"), (15, "Более 15%")]

    rc = forms.IntegerField(
        widget=forms.RadioSelect(choices=revc))


class CredLine(forms.Form):
    crl = [(8, "8-10%"), (11, "11-13%"), (14, "14-15%"), ]

    cl = forms.IntegerField(
        widget=forms.RadioSelect(choices=crl))


class RevCredLine(forms.Form):
    revcl = [(8, "8-9%"), (10, "10-11%"), (15, "Более 12%")]

    rcl = forms.IntegerField(
        widget=forms.RadioSelect(choices=revcl))


class InvestCredLine(forms.Form):
    icl = [(8, "8-9%"), (10, "10-11%"), (15, "Более 12%")]

    invecstcl = forms.IntegerField(
        widget=forms.RadioSelect(choices=icl))


class CredIP(forms.Form):
    cip = [(8, "8-9%"), (10, "10%"), (11, "11%")]

    crep = forms.IntegerField(
        widget=forms.RadioSelect(choices=cip))


class CredIPProp(forms.Form):
    cipp = [(8, "8-9%"), (10, "10%"), (11, "11%")]

    cripp = forms.IntegerField(
        widget=forms.RadioSelect(choices=cipp))


class BankFuncCorp(forms.Form):
    bfc = [("account", "Открытие и обслуживание счета"), ("overdraft", "Овердрафт"), ("expcred", "Экспресс кредит"),
           ("intavail", "Возможность размещения средств в интернет банке"),
           ("salprojavail", "Наличие зарплатного проекта"), ("deposits", "Депозиты"),
           ("intappavail", "Наличие интернет приложения"), ]

    bfcp = forms.MultipleChoiceField(choices=bfc,
                                     widget=forms.CheckboxSelectMultiple)
