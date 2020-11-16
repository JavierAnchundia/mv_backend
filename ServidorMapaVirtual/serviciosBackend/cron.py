import datetime

from django.core.mail import send_mail
from django.http import HttpResponse
from pyfcm import FCMNotification

from ServidorMapaVirtual import settings
from .serializers import FavoritosFullSerializer, Token_DeviceSerializer
from .models import Favoritos, TokenDevice

def enviarPush(reg_id,title,message, difunto):
    push_service = FCMNotification(api_key="AAAA24gEGpE:APA91bGYzC5BiDTiCWM2diwEgoC_Rwt8iRXibonufzoNUbkHCzsuUcfH_6P3pjtv7CfQBveZWqJxWB4iIAOPXJulI6DiVFxk6vgVvex5Zdn3Du42i98h9ja49SsE-FDetubvLycsjynY")
    data_message={
        "message": message,
        "difunto": difunto
    }
    result = push_service.notify_single_device(
                                    registration_id=reg_id,
                                    message_title=title,
                                    message_body=message,
                                    data_message = data_message
                                )
    print(result)
    return result

def notificacion_cumpleanos():
    today_day = datetime.date.today().day
    today_month = datetime.date.today().month
    qs = Favoritos.objects.filter(id_difunto__fecha_nacimiento__day = today_day, id_difunto__fecha_nacimiento__month= today_month)
    token = "fs1GQdzSRFSiwh8GhhHL8M:APA91bHx7FYXmw-W7rLhSfmjtxsSksJ3icY9ysPecQwB3JvOfSizRGRjB3yFvV0Xxt7LhEmYQsPchO99pL47DnSu4LSMt5EiBJW-U8j4X8PhjI_AHhwVK81gRhpUYNOSN4SoVV44_kjD"
    for i in list(qs):
        i=FavoritosFullSerializer(i)
        title = "Recordatorio de cumpleaños de " + i.data['id_difunto']['nombre'] +' '+ i.data['id_difunto']['apellido']
        message = "Recuerda a tu ser querido en este día.Déjale un mensaje."
        user = TokenDevice.objects.filter(id_user= i.data['id_usuario']).values('token_device')
        '''enviarPush(user[0]['token_device'],title,message, i.data['id_difunto'])'''
        enviarPush(token, title, message, i.data['id_difunto'])
        print(user[0]['token_device'])
        print(i.data['id_difunto'])
        print(title)
    return HttpResponse(list(qs))

def aniversario_defuncion():
    today_day = datetime.date.today().day
    today_month = datetime.date.today().month

    qs = Favoritos.objects.filter(id_difunto__fecha_difuncion__day = today_day, id_difunto__fecha_difuncion__month= today_month)
    for i in list(qs):
        i = FavoritosFullSerializer(i)
        title = "Aniversario de defunción de " + i.data['id_difunto']['nombre'] + ' ' + i.data['id_difunto'][
            'apellido']
        message = "Recuerda a tu ser querido en este día. Déjale un mensaje."
        user = TokenDevice.objects.filter(id_user=i.data['id_usuario']).values('token_device')
        enviarPush(user[0]['token_device'], title, message, i.data['id_difunto'])
        print(user[0]['token_device'])
        print(title)

    return HttpResponse(list(qs))

