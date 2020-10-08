from django.contrib import admin
from serviciosBackend.models import User,Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos, Homenajes, H_mensaje, H_imagen, H_video,H_audio, Historial_rosas
myModels = [User, Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos,Homenajes, H_mensaje, H_imagen, H_video,Historial_rosas,H_audio]  # iterable list
admin.site.register(myModels)
