from django.contrib import admin
from .models import User,Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos, Homenajes, H_mensaje, H_imagen, H_video,H_audio, Historial_rosas, TokenDevice
myModels = [User, Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos,Homenajes, H_mensaje, H_imagen, H_video, Historial_rosas, H_audio, TokenDevice]  # iterable list
admin.site.register(myModels)
