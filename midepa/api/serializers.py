from rest_framework import serializers
from django.contrib.auth.models import User

from midepa.models import (
    Profile,
    Condominio,
    Presupuesto,
    Servicio
)

class UserSerializer(serializers.ModelSerializer):
    '''User Serializer'''
    class Meta:
        model = User
        fields = ('id', 'username', 'password')



class ProfileSerializer(serializers.ModelSerializer):
    '''Profile Serializer'''
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = ('user',
                  'is_admin',
                  'avatar',
                  'first_name',
                  'last_name',
                  'apartment_number',
                  'email',
                  'rating',
                  'phone')


class RegistrationSerializer(serializers.Serializer):
    '''Registration Serializer'''
    username = serializers.CharField(max_length=90)
    password = serializers.CharField(max_length=90)
    first_name = serializers.CharField(max_length=90)
    last_name = serializers.CharField(max_length=90)
    is_admin = serializers.BooleanField(default=False)
    email = serializers.EmailField()


class CondominioSerializer(serializers.ModelSerializer):
    '''Condominio Serializer'''
    class Meta:
        model = Condominio
        fields = ('id', 'name')


class ServicioSerializer(serializers.ModelSerializer):
    '''Servicios Serializer'''

    class Meta:
        model = Servicio
        fields = ('id',
                  'presupuesto',
                  'condominio',
                  'name',
                  'price',
                  'rating',
                  'company_name',
                  'description')


class PresupuestoSerializer(serializers.ModelSerializer):
    '''Presupuesto Serializer'''
    condominio = CondominioSerializer(read_only=True)
    servicios = ServicioSerializer(many=True, read_only=True)

    class Meta:
        model = Presupuesto
        fields = ('id',
                  'month',
                  'condominio',
                  'apartments',
                  'budget',
                  'servicios')
