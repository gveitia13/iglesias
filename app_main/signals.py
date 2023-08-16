from django.db.models.signals import post_save
from django.dispatch import receiver

from app_main.models import Presbiterio


@receiver(post_save, sender=Presbiterio)
def update_distrito_cant_presbiterios(sender, instance, **kwargs):
    distrito = instance.distrito
    distrito.cant_presbiterios = distrito.presbiterio_set.count()
    distrito.save()
