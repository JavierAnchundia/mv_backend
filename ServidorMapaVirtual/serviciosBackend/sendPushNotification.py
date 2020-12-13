# !/usr/bin/python3.8
import os, sys
from dotenv import load_dotenv
from django.db.models import Q
import schedule
import time
from datetime import datetime, timedelta
from .models import User, TokenDevice
from .serializers import UserProfileSerializer, Token_DeviceSerializer
from django.http import HttpResponse
from pyfcm import FCMNotification
load_dotenv()

def sendNotificaction(id_camposanto, title, body):
    try:
        push_service = FCMNotification(api_key=os.getenv("FCM_KEY"))
        registration_ids = []
        usuarios = User.objects.filter(Q(id_camposanto=id_camposanto))
        for usuario in usuarios:
            userSerializer = UserProfileSerializer(usuario)
            id_user = userSerializer['id'].value
            token = TokenDevice.objects.filter(Q(id_user=id_user))
            if(len(token) > 0):
                tokens_serializer = Token_DeviceSerializer(token[0])
                registration_ids.append(tokens_serializer['token_device'].value)

        data_message = {
            "title": title,
            "message": body
        }

        result = push_service.notify_multiple_devices(
            registration_ids=registration_ids,
            message_title=title,
            message_body=body,
            data_message=data_message
        )
        print(result)
        time.sleep(5)
        return 1
    except Exception:
        return 0