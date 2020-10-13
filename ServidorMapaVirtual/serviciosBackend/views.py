from django.http import HttpResponse, Http404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from .servicioFacebook import Facebook
from .get_jwt_user import Json_web_token
from django.shortcuts import get_object_or_404

from rest_framework.renderers import (HTMLFormRenderer,
                                        JSONRenderer,
                                        BrowsableAPIRenderer,)
from .models import User, Empresa, Red_social, Camposanto, Punto_geolocalizacion, Sector, Tipo_sepultura, Responsable_difunto, Difunto, Permiso, User_permisos, Homenajes, H_mensaje, H_imagen, H_video, Historial_rosas, H_audio
from .serializers import UserProfileSerializer, EmpresaSerializer, Red_socialSerializer, CamposantoSerializer, Punto_geoSerializer, SectorSerializer, Tipo_sepulturaSerializer, Responsable_difuntoSerializer, DifuntoSerializer, PermisoSerializer, User_permisosSerializer, HomenajeSerializer, H_mensajeSerializer, H_imagenSerializer, H_audioSerializer ,H_videoSerializer, HomenajeSimpleSerializer, Historial_rosasSerializer,Log_RosasSerializer

'''API Rest get unico, get list, post y put para Camposanto'''
class CamposantoView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        camposantoObj = Camposanto.objects.all()
        serializer = CamposantoSerializer(camposantoObj, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CamposantoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CamposantoViewSet(APIView):
    def get_object(self, pk):
        try:
            return Camposanto.objects.get(id_camposanto=pk)
        except Camposanto.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        camposantoObj = self.get_object(pk)
        serializer = CamposantoSerializer(camposantoObj)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        camposantoObj = self.get_object(pk)
        serializer = CamposantoSerializer(camposantoObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''API Rest getList, post y put para Red_social'''
class Red_socialPost(APIView):
    def post(self, request, format=None):
        serializer = Red_socialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Red_socialListGet(APIView):
    def get(self, request, id_camp, format=None):
        red_socialObj = Red_social.objects.filter(id_camposanto=id_camp)
        serializer = Red_socialSerializer(red_socialObj, many=True)
        return Response(serializer.data)

class Red_socialPut(APIView):
    def get_objects(self, id_red):
        try:
            return Red_social.objects.get(id_camposanto=id_red)
        except Red_social.DoesNotExist:
            raise Http404
    def put(self, request, id_red, format=None):
        red_socialObj  = self.get_object(id_red)
        serializer = Red_socialSerializer(red_socialObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''API Rest post y getList para Geolocalizacion'''
class GeolocalizacionPost(APIView):
    def post(self, request, format=None):
        serializer = Punto_geoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GeolocalizacionListGet(APIView):
    def get(self, request, id_camp, format=None):
        geolocalizacionObj = Punto_geolocalizacion.objects.filter(id_camposanto=id_camp)
        serializer = Punto_geoSerializer(geolocalizacionObj, many=True)
        return Response(serializer.data)

class GeolocalizacionDelete(APIView):
    def get_object(self, id_punto):
        try:
            return Punto_geolocalizacion.objects.get(id_punto=id_punto)
        except Punto_geolocalizacion.DoesNotExist:
            raise Http404
    def delete(self, request, id_punto, format=None):
        geolocalizacionObj = self.get_object(id_punto)
        geolocalizacionObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''API Rest get para Sector'''
class SectorListGet(APIView):
    def get(self, request, id_camp, format=None):
        sectorObj = Sector.objects.filter(id_camposanto=id_camp)
        serializer = SectorSerializer(sectorObj, many=True)
        return Response(serializer.data)

'''API Rest get para Tipo Sepultura'''
class Tipo_sepulturaListGet(APIView):
    def get(self, request, id_camp, format=None):
        tiposObj = Tipo_sepultura.objects.filter(id_camposanto=id_camp)
        serializer = Tipo_sepulturaSerializer(tiposObj, many=True)
        return Response(serializer.data)

'''API Rest get unico, get list, post y put para Difunto'''
class DifuntoView(APIView):
    def post(self, request, format=None):
        serializer = DifuntoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DifuntoListGet(APIView):
    def get(self, request, id_camp, format=None):
        difuntosObj = Difunto.objects.filter(Q(id_camposanto=id_camp))
        serializer = DifuntoSerializer(difuntosObj, many=True)
        return Response(serializer.data)

class DifuntoListFilteredGet(APIView):
    def get(self, request, id_camp, nombre, apellido, format=None):
        difuntosObj = Difunto.objects.filter(Q(id_camposanto=id_camp) & (Q(nombre=nombre) | Q(apellido=apellido)))
        serializer = DifuntoSerializer(difuntosObj, many=True)
        return Response(serializer.data)

'''API Rest get unico, post para Responsable'''
class Responsable_difuntoView(APIView):
    def post(self, request, format=None):
        serializer = Responsable_difuntoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Responsable_difuntoViewSet(APIView):
    def get_object(self, id_difunto):
        try:
            return Responsable_difunto.objects.get(id_difunto=id_difunto)
        except Responsable_difunto.DoesNotExist:
            raise Http404
    def get(self, request, id_difunto, format=None):
        responsableObj = self.get_object(id_difunto)
        serializer = Responsable_difuntoSerializer(responsableObj)
        return Response(serializer.data)
    
    def put(self, request, id_difunto, format=None):
        responsableObj = self.get_object(id_difunto)
        serializer = Responsable_difuntoSerializer(responsableObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''API Rest get list y get id para empresa'''
class EmpresasView(APIView):
    def get(self, request, format=None):
        empresaObj = Empresa.objects.all()
        serializer = EmpresaSerializer(empresaObj, many=True)
        return Response(serializer.data)

class EmpresaViewSet(APIView):
    def get_object(self, pk):
        try:
            return Empresa.objects.get(id_empresa=pk)
        except Empresa.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        empresaObj = self.get_object(pk)
        serializer = EmpresaSerializer(empresaObj)
        return Response(serializer.data)
    # el siguiente metodo se debe incluir
    def put(self, request, pk, format=None):
        empresaObj = self.get_object(pk)
        serializer = EmpresaSerializer(empresaObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     hasta aqui

class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'GET':
            permission_classes = [AllowAny ]
        if self.action == 'create':
            permission_classes = [AllowAny]

        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# obtener lista de usuarios por camposanto
class UsuarioGetCamposanto(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, id_camp, format=None):
        usuariosObj = User.objects.filter(id_camposanto=id_camp)
        serializer = UserProfileSerializer(usuariosObj, many=True)
        return Response(serializer.data)

# para validar en el registro de usuarios si un username o email por camposanto ya esta usado
class UsuarioGetAll(APIView):
    def get(self, request, format=None):
        usuarioObj = User.objects.all()
        for userO in usuarioObj:
            userO.first_name = ''
            userO.last_name = ''
            userO.telefono = ''
            userO.genero = ''
            userO.direccion = ''
            userO.staff = ''
            userO.tipo_usuario = ''
        serializer = UserProfileSerializer(usuarioObj, many=True)
        return Response(serializer.data)

# Api para obtener permisos
class PermisoView(APIView):
    def get(self, request, format=None):
        permisoObj = Permiso.objects.all()
        serializer = PermisoSerializer(permisoObj, many=True)
        return Response(serializer.data)

    


# Crear usuarios con sus respectivos permisos
class User_PermisosPost(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = User_permisosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Create_User_Facebook(APIView):
    def post(self, request, format=None):
        access_token = request.data['access_token']
        # instancia de la clase facebook
        f = Facebook()
        # se obtienen los datos a traves de la api de facebook
        data = f.get_info_facebook(access_token)
        # instancia de la clase Json_web_token
        jwt = Json_web_token()
        # validar que no existe dicho usuarios guardado
        usuario_validate = self.obtener_User(data['username'])

        if usuario_validate:
            token = jwt.get_token_user(usuario_validate)
            return Response(token, status=status.HTTP_201_CREATED)
        else:
            user_serializer = UserProfileSerializer(data= data)
            if user_serializer.is_valid():
                user_save = user_serializer.save()
                if user_save :
                    # instancia de la clase Json_web_token
                    jwt = Json_web_token()
                    token = jwt.get_token_user(user_save)
                return Response(token, status=status.HTTP_201_CREATED)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def obtener_User(self, username):
        try:
            return User.objects.get(username = username)
        except User.DoesNotExist:
            return None

#PENDIENTE DE AGREGAR A PA #################################################################################################

#Este VIEW es todo nuevo
class Permiso_Info(APIView):
    def get_object(self,pk):
        try:
            return Permiso.objects.get(id_permiso=pk)
        except Permiso.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        permisoObj = self.get_object(pk)
        serializer = PermisoSerializer(permisoObj)
        return Response(serializer.data)

# Obtener permisos de un usuario // Cambie el algo del metodo get_object y anadi el metodo delete
class User_PermisosGet(APIView):
    def get_object(self, pk):
        try:
            return User_permisos.objects.get(id_difunto=pk)
        except Difunto.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user_permisosObj = User_permisos.objects.filter(Q(id_user=id))
        serializer = User_permisosSerializer(user_permisosObj, many=True)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        user_permisosObj = (User_permisos.objects.filter(Q(id_user=id))).delete()
        return Response(user_permisosObj)


class UsuarioViewGet(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
    def get(self, request, username, format=None):
        usuarioObj = self.get_object(username)
        serializer = UserProfileSerializer(usuarioObj)
        return Response(serializer.data)
    # parte nueva para actualizar usuario seteando el password, este metodo se incluye en lo del PythonAnyWhere
    def put(self, request, username, format = None):
        usuarioObj = self.get_object(username)
        if 'password' in request.data:
            if(request.data['password']):
                new_password = request.data['password']
                usuarioObj.set_password(new_password)
                request.data['password'] = usuarioObj.password
        serializer = UserProfileSerializer(usuarioObj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DifuntoViewSet(APIView):
    def get_object(self, pk):
        try:
            return Difunto.objects.get(id_difunto=pk)
        except Difunto.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        difuntoObj = self.get_object(pk)
        serializer = DifuntoSerializer(difuntoObj)
        return Response(serializer.data)
    #Aqui es el meotod PUT lo nuevo
    def put(self, request, pk, format=None):
        difuntoObj = self.get_object(pk)
        serializer = DifuntoSerializer(difuntoObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Homenaje_Get(APIView):
    def get(self, request, id, format=None):
        user_homenajesObj = Homenajes.objects.filter(Q(id_difunto=id))
        serializer = HomenajeSerializer(user_homenajesObj, many=True)
        return Response(serializer.data)

class Homenaje_Set(APIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = HomenajeSimpleSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def post(self, request, format=None):
        serializer = HomenajeSimpleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Himagen_Get(APIView):
    def get(self, request, id, format=None):
        user_HimagenObj = H_imagen.objects.filter(Q(id_homenaje=id))
        serializer = H_imagenSerializer(user_HimagenObj, many=True)
        return Response(serializer.data)


class Htexto_Get(APIView):
    def get(self, request, id, format=None):
        user_HtextoObj = H_mensaje.objects.filter(Q(id_homenaje=id))
        serializer = H_mensajeSerializer(user_HtextoObj, many=True)
        return Response(serializer.data)

class Htexto_Set(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = H_mensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Himagen_Set(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = H_imagenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Hvideo_Set(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = H_videoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener contenido de audio para homenaje
class Haudio_Get(APIView):
    def get(self, request, id, format=None):
        Haudio_obj = H_audio.objects.filter(Q(id_homenaje=id))
        serializer = H_audioSerializer(Haudio_obj, many=True)
        return Response(serializer.data)

# Crear contenido de audio para homenaje
class Haudio_Set(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = H_audioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AmountPartialUpdateView(APIView):

    def patch(self, request, pk, num_rosas):
        model = get_object_or_404(Difunto, pk=pk)
        data = {"num_rosas": model.num_rosas + int(num_rosas)}
        serializer = DifuntoSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Historial_rosasGet(APIView):
    def get(self, request, id, format=None):
        historial_Obj = Historial_rosas.objects.filter(Q(id_difunto=id))
        serializer = Log_RosasSerializer(historial_Obj, many=True)
        return Response(serializer.data)

class Historial_rosasSet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = Historial_rosasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

