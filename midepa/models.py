from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ''' Profile Model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    avatar = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    apartment_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    rating = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return self.email


class Condominio(models.Model):
    ''' Condominop Model '''
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Presupuesto(models.Model):
    ''' Presupuesto Model '''
    month = models.CharField(max_length=90)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    apartments = models.PositiveIntegerField(default=0)
    budget = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.month


class Servicio(models.Model):
    ''' Servicio Model '''
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE, related_name="servicios")
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name="servicios")
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    company_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name



