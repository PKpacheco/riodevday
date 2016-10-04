# coding: utf-8

from django.db import models
from core.models import TimeStampedModel


class Sponsor(TimeStampedModel):

    name = models.CharField(max_length=255, verbose_name="Nome")
    photo = models.ImageField(upload_to='colaborator/', verbose_name='Foto', blank=True, null=True)
    social_network = models.URLField(max_length=255, verbose_name="Rede Social", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Patrocinador'
        verbose_name_plural = 'Patrocinadores'
