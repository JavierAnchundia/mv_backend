from rest_framework import serializers
from .models import User, Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos
from django.conf import settings
from django.core.mail import send_mail

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class Red_socialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Red_social
        fields = '__all__'

class CamposantoSerializer(serializers.ModelSerializer):
    # id_empresa = EmpresaSerializer(read_only=True)
    class Meta:
        model = Camposanto
        fields = '__all__'

class Punto_geoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punto_geolocalizacion
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class Tipo_sepulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_sepultura
        fields = '__all__'

# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = '__all__'

class Responsable_difuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable_difunto
        fields = '__all__'

class DifuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difunto
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'telefono',
            'genero',
            'direccion',
            'id_camposanto',
            'staff',
            'tipo_usuario'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.username = validated_data.get('username')
        user.set_password(password)
        validar = user.save()
        if(validar == None):
            camposanto = self.obtener_camposanto(user)
            self.send_email(user, camposanto)
        return user

    def obtener_camposanto(self, usuario):
        retorno = ''
        camposanto = usuario.id_camposanto
        if(camposanto):
            nombreCamposanto = camposanto.nombre
            retorno = nombreCamposanto
        return retorno

    def send_email(self, usuario, camposanto):
        subject = '¡Bienvenido a Mapa Virtual!'
        if(camposanto and usuario.first_name and usuario.last_name):
            message = '¡Te damos la bienvenida a mapa virtual! \n'\
                      'Hola ' + usuario.first_name + ' ' + usuario.last_name+',\n'\
                      'Gracias por unirte a '+ camposanto +'.\n' \
                      '\nExplora nuestra página y conoce más novedades. '
        else:
            message = 'Bienvenido '+ usuario.email +', gracias por registrarse !!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [usuario.email, ]
        send_mail(subject, message, email_from, recipient_list)

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class User_permisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_permisos
        fields = '__all__'