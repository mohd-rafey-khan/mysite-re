# i created this page
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzer(request):
    var = request.GET.get('text1','default')
    uppercase_var  = request.GET.get('uppercase','off')
    removepunc_var = request.GET.get('removepunc', 'off')
    removenewline_var = request.GET.get('removenewline', 'off')
    upr_lwr_var = request.GET.get('upr_lwr', 'off')
    if(uppercase_var == 'on'):
        fnl_var = ""
        for bit in var:
            fnl_var += bit.upper()
        var = fnl_var
    if(upr_lwr_var == 'on'):
        fnl_var = ""
        for bit in var:
            if bit.islower():
                fnl_var += bit.upper()
            elif bit.isupper():
                fnl_var += bit.lower()
            else:
                fnl_var += bit
        var = fnl_var
    if(removepunc_var == 'on'):
        fnl_var = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for bit in var:
            if bit not in punc:
                fnl_var += bit
        var = fnl_var
    if(removenewline_var == 'on'):
        fnl_var = ""
        for bit in var:
            if bit == "/n":
                fnl_var += " "
            else:
                fnl_var += bit
        var = fnl_var

    params = {'return_var':var}
    return render(request,'analyse.html',params)