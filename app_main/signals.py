from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from app_main.models import Presbiterio


def calculate(instance):
    distrito = instance.user.distrito
    distrito.cant_presbiterios = instance.user.presbiterio_set.count()
    distrito.presbiteriales = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('presbiteriales')])
    distrito.nacionales = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('nacionales')])
    distrito.licenciados = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('licenciados')])
    distrito.ordenados = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('ordenados')])
    distrito.total_cuerpo_ministerial = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('total_cuerpo_ministerial')])
    distrito.templos_oficiales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('templos_oficiales')])
    distrito.templos_no_oficiales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('templos_no_oficiales')])
    distrito.casa_templo = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('casa_templo')])
    distrito.tabernaculos = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('tabernaculos')])
    distrito.casas_pastorales = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('casas_pastorales')])
    distrito.iglesias = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('iglesias')])
    distrito.misiones = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('misiones')])
    distrito.casas_cultos = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('casas_cultos')])
    distrito.ministros = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('ministros')])
    distrito.miembros = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('miembros')])
    distrito.visitantes = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('visitantes')])
    distrito.ninnos = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('ninnos')])
    distrito.total_afiliacion_oficial = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('total_afiliacion_oficial')])
    distrito.jovenes = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('jovenes')])
    distrito.damas = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('damas')])
    distrito.caballeros = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('caballeros')])
    distrito.total_departamento = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('total_departamento')])
    distrito.promedio_asistencia = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('promedio_asistencia')])
    distrito.bautizados_espiritu = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('bautizados_espiritu')])
    distrito.lideres_locales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('lideres_locales')])
    distrito.obreros_tiempo_completo = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('obreros_tiempo_completo')])
    distrito.estudiantes = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('estudiantes')])
    distrito.save()


@receiver(post_save, sender=Presbiterio)
def update_distrito_on_save_presbiterios(sender, instance, **kwargs):
    calculate(instance)


@receiver(post_delete, sender=Presbiterio)
def update_distrito_on_delete_presbiterios(sender, instance, *args, **kwargs):
    calculate(instance)