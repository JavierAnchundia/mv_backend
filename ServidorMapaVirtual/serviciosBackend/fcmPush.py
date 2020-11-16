from pyfcm import FCMNotification

def enviarPush():
    push_service = FCMNotification(api_key="AAAA24gEGpE:APA91bGYzC5BiDTiCWM2diwEgoC_Rwt8iRXibonufzoNUbkHCzsuUcfH_6P3pjtv7CfQBveZWqJxWB4iIAOPXJulI6DiVFxk6vgVvex5Zdn3Du42i98h9ja49SsE-FDetubvLycsjynY")
    registration_id = "cEZSFBMrSuypYmkH8UOTD8:APA91bGA1dko7G3b90BJUhHBNEzbEzlxWel9F6VwVjUPUJZhg0NXvpMB_UvrIFBDDlkoOrIOXZ8ymtvkbDAKqXQn2e_NsWkLZUmPR82eWroyWs41-2t7RtoTuBbfuLY4MP7n2BwLvskn"
    message_title = "Mapa virtual"
    data_message = {
        "icon_url": "https://image.flaticon.com/icons/png/512/22/22744.png"
    }
    message_body = "Hola Bryan Ionic"
    result = push_service.notify_single_device(
                                    registration_id=registration_id,
                                    message_title=message_title,
                                    message_body=message_body,
                                    data_message = data_message
                                )
    print(result)
    return result

enviarPush()