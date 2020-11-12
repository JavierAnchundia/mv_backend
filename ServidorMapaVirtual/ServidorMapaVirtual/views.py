from django.http import  HttpResponse
from django.shortcuts import render
# 10/11/2020
def RecuperarContrasena(request, id_user, token):
    return render(request, 'recuperarContrasena.html', {"user": id_user, "token": token})

