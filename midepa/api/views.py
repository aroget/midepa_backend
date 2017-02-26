from django.contrib.auth.models import User
from rest_framework import generics
from django.http import Http404
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


from midepa.models import (Profile,
                           Condominio,
                           Presupuesto,
                           Servicio)


from .serializers import (RegistrationSerializer,
                          CondominioSerializer,
                          PresupuestoSerializer,
                          ServicioSerializer,
                          ProfileSerializer)

MAX_RATING = 5

'''
Sign up, both admin and non admin, admin role
is specified by the is_admin field defaults to False
'''
class RegistrationCreateAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(RegistrationCreateAPIView, self).get_serializer(*args, **kwargs)

    def do_registration(self, user_data):
        user = User.objects.create_user(username=user_data['username'],
                                        password=user_data['password'])

        user.set_password(user_data['password'])
        user.save()

        profile = Profile.objects.create(user=user,
                                         is_admin=user_data['is_admin'],
                                         first_name=user_data['first_name'],
                                         last_name=user_data['last_name'],
                                         email=user_data['email'])
        profile.save()

        if user_data['is_admin']:
            condominio = Condominio.objects.create(owner=user,
                                                   name=user_data['username'])
            condominio.save()

    def perform_create(self, serializer):
        try:
            self.do_registration(serializer.data)
        except TypeError:
            for user_data in serializer.data:
                self.do_registration(user_data)


'''
Lists all inquilinos on file, except the currently
logged in user, in case the user does not have is_admin
set to True returns 404
'''
class InquilinosListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)

        if profile.is_admin:
            return Profile.objects.all().exclude(user=user)
        else:
            raise Http404

'''
Returns the currently logged in user's profile
'''
class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


'''
Creates a Presupuesto
'''
class PresupuestoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PresupuestoSerializer
    queryset = Presupuesto.objects.all()

    def perform_create(self, serializer):
        condominio_id = self.request.data['condominio']
        condominio = Condominio.objects.get(id = condominio_id)
        serializer.save(condominio = condominio)


'''
DELETE, PATCH, GET for single presupuesto
'''
class PresupuestoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PresupuestoSerializer
    queryset = Presupuesto.objects.all()


'''
Creates a Servicio
'''
class ServicioListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(ServicioListCreateAPIView, self).get_serializer(*args, **kwargs)


'''
Rate service
'''
class ServicioRatingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()

    def partial_update(request, *args, **kwargs):
        servicio_id = kwargs['pk']
        servicio = get_object_or_404(Servicio, pk=servicio_id)

        servicio.rating = servicio.rating + 1
        servicio.save()

        return Response({}, status=status.HTTP_202_ACCEPTED)

        # print(servicio)


'''
DELETE, PATCH, GET for single Servicio
'''
class ServicioLRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()


'''
GET Condominio's details
'''
class CondominioAPIView(generics.ListAPIView):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()
