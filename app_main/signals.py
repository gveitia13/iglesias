from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from app_main.models import Presbiterio


# @receiver(post_save, sender=Presbiterio)
# def update_distrito_on_save_presbiterios(sender, instance, **kwargs):
#     distrito = instance.distrito
#     distrito.cant_presbiterios = distrito.presbiterio_set.count()
#     distrito.save()


# @receiver(post_delete, sender=Presbiterio)
# def update_distrito_on_delete_presbiterios(sender, instance, *args, **kwargs):
#     distrito = instance.distrito
#     distrito.cant_presbiterios = distrito.presbiterio_set.count()
#     distrito.save()
