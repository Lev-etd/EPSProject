from django.db import models
from django import forms


# Create your models here.


class Bank_ind(models.Model):
    name = models.CharField(max_length=100, null=True)
    security = models.CharField(max_length=100, null=True)
    CrCardExist = models.BooleanField(max_length=100, null=True)
    DebCardExist = models.CharField(max_length=100, null=True)
    PremCardExist = models.CharField(max_length=100, null=True)
    RubDep = models.CharField(max_length=100, null=True)
    DolDep = models.CharField(max_length=100, null=True)
    EurDep = models.CharField(max_length=100, null=True)
    MultivDepExist = models.BooleanField(max_length=100, null=True)
    CrRealEstate = models.CharField(max_length=100, null=True)  # sometimes equals to zero
    CrWtLoan = models.CharField(max_length=100, null=True)  # sometimes equals to zero
    CrRealEstateAuto = models.CharField(max_length=100, null=True)  # sometimes equals to zero
    Refinancing = models.BooleanField(max_length=100, null=True)
    AutoCr = models.CharField(max_length=100, null=True)  # sometimes equals to zero
    Deposits = models.BooleanField(max_length=100, null=True)
    Insurance = models.BooleanField(max_length=100, null=True)
    Investments = models.BooleanField(max_length=100, null=True)
    MobApp = models.BooleanField(max_length=100, null=True)
    MobConn = models.BooleanField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Bank_legal(models.Model):
    name = models.CharField(max_length=100)
    opening = models.BooleanField(max_length=100)
    revLoan = models.CharField(max_length=100)
    CreditLine = models.CharField(max_length=100)
    RevCreditLine = models.CharField(max_length=100)
    InvestCreditLine = models.CharField(max_length=100)
    AnyCredit = models.CharField(max_length=100)
    AnyCreditEstate = models.CharField(max_length=100)
    Overdraft = models.BooleanField(max_length=100)
    Deposits = models.BooleanField(max_length=100)  # sometimes equals to zero
    MobBank = models.BooleanField(max_length=100)  # sometimes equals to zero
    Security = models.CharField(max_length=100)  # sometimes equals to zero

    def __str__(self):
        return self.name


class Bank_corp(models.Model):
    name = models.CharField(max_length=100)
    opening = models.BooleanField(max_length=100)
    ExpCred = models.BooleanField(max_length=100)
    Overdraft = models.BooleanField(max_length=100)
    IntPlace = models.BooleanField(max_length=100)
    SalProj = models.BooleanField(max_length=100)
    Deposits = models.BooleanField(max_length=100)
    WebApp = models.BooleanField(max_length=100)
    Security = models.CharField(max_length=100)

    def __str__(self):
        return self.name


