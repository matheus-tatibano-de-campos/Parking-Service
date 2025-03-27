from django.db import models

from customers.models import Customer


class VehicleType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Nome',
    )
    description = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Descrição',
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name='Tipo de Veículo',
        verbose_name_plural="Tipos de Veiculos"

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type= models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo Do Veículo',
    )
    license_plate =models.CharField(
     max_length=10,
        unique=True,
        verbose_name='Placa'
    )
    brand = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Marca',
    )
    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Marca',
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Marca',
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Propietário'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name='Veículo',
        verbose_name_plural="Veiculos"

    def __str__(self):
        return self.license_plate
