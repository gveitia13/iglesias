from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from app_main.models import Presbiterio


def calculate(instance):
    distrito = instance.user.distrito
    distrito.cant_presbiterios = instance.user.presbiterio_set.count()

    distrito.presbiteriales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('presbiteriales') if i[0]])
    distrito.nacionales = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('nacionales') if i[0]])
    distrito.licenciados = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('licenciados') if i[0]])
    distrito.ordenados = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('ordenados') if i[0]])
    distrito.total_cuerpo_ministerial = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('total_cuerpo_ministerial') if i[0]])
    distrito.templos_oficiales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('templos_oficiales') if i[0]])
    distrito.templos_no_oficiales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('templos_no_oficiales')])
    distrito.casa_templo = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('casa_templo') if i[0]])
    distrito.tabernaculos = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('tabernaculos') if i[0]])
    distrito.casas_pastorales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('casas_pastorales') if i[0]])
    distrito.iglesias = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('iglesias') if i[0]])
    distrito.misiones = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('misiones') if i[0]])
    distrito.casas_cultos = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('casas_cultos') if i[0]])
    distrito.ministros = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('ministros') if i[0]])
    distrito.miembros = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('miembros') if i[0]])
    distrito.visitantes = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('visitantes') if i[0]])
    distrito.ninnos = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('ninnos') if i[0]])
    distrito.total_afiliacion_oficial = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('total_afiliacion_oficial') if i[0]])
    distrito.jovenes = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('jovenes') if i[0]])
    distrito.damas = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('damas') if i[0]])
    distrito.caballeros = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('caballeros') if i[0]])
    distrito.total_departamento = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('total_departamento') if i[0]])
    distrito.promedio_asistencia = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('promedio_asistencia') if i[0]])
    distrito.bautizados_espiritu = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('bautizados_espiritu') if i[0]])
    distrito.lideres_locales = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('lideres_locales') if i[0]])
    distrito.obreros_tiempo_completo = sum(
        [i[0] for i in instance.user.presbiterio_set.all().values_list('obreros_tiempo_completo') if i[0]])
    distrito.estudiantes = sum([i[0] for i in instance.user.presbiterio_set.all().values_list('estudiantes') if i[0]])
    distrito.save()


@receiver(post_save, sender=Presbiterio)
def update_distrito_on_save_presbiterios(sender, instance, **kwargs):
    calculate(instance)


@receiver(post_delete, sender=Presbiterio)
def update_distrito_on_delete_presbiterios(sender, instance, *args, **kwargs):
    calculate(instance)
