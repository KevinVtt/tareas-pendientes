from typing import Any
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Tarea(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['completo']


class NumerosTelefonicos(models.Model):
    usuario = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    numero_telefono = models.CharField(max_length=11)
    nacionalidad = CountryField()
    fecha_nacimiento = models.DateField(null=False,
                                        blank=False)
    numero_area = models.IntegerField(verbose_name="Numero de Area",
                                      validators=[MinValueValidator(0), MaxValueValidator(999)])

    class Meta:
        ordering = ['numero_telefono']

    def __str__(self):
        return self.numero_telefono
    