from django.contrib import admin
from serviciosBackend.models import User,Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos, Homenaje
myModels = [User, Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos, Homenaje]  # iterable list
admin.site.register(myModels)