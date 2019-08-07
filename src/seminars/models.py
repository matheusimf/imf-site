# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class ClassMaterial(models.Model):
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.material


class SeminarType(models.Model):
    THETAHEALING = 0
    ACCESS = 1
    MODALITY_CHOICES = (
        (THETAHEALING, 'ThetaHealing'),
        (ACCESS, 'Access Consciousness'),
    )
    BRL = 0
    USD = 1
    CURRENCY_CHOICES = (
        (BRL, 'Real'),
        (USD, 'Dólar')
    )
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=50)
    modality = models.IntegerField(choices=MODALITY_CHOICES, default=0)
    materials = models.ManyToManyField(ClassMaterial, blank=True)
    prerequisites = models.ManyToManyField(
        "self", through='SeminarTypePrerequisite',
        symmetrical=False, blank=True
    )
    image_url = models.CharField(max_length=100, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    early_inscription_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    inscription_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    price_parts = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    max_number_parts = models.IntegerField(blank=True, null=True)
    currency = models.IntegerField(choices=CURRENCY_CHOICES, default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class SeminarTypePrerequisite(models.Model):
    from_seminartype = models.ForeignKey(
        SeminarType, related_name='from_seminartype', on_delete=models.CASCADE
    )
    to_seminartype = models.ForeignKey(
        SeminarType, related_name='to_seminartype', on_delete=models.CASCADE
    )


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    seminars_teach = models.ManyToManyField(SeminarType)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SeminarLocation(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(blank=True, null=True)
    complement = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Seminar(models.Model):
    ACTIVE = 0
    COMPLETED = 1
    CANCELED = 2
    STATUS_CHOICES = (
        (ACTIVE, 'Ativo'),
        (COMPLETED, 'Completo'),
        (CANCELED, 'Cancelado')
    )
    seminar_type = models.ForeignKey(SeminarType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(SeminarLocation, on_delete=models.DO_NOTHING,
                                 blank=True, null=True)
    instructor = models.ManyToManyField(Instructor, blank=True)
    date_time_info = models.CharField(max_length=255, blank=True)
    seminar_status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        date = self.start_date.strftime('%d/%m/%y')
        seminar_name = self.seminar_type.name
        return date + ' - ' + seminar_name
