from django.contrib import messages
from django.shortcuts import redirect

from app_main.models import ResumenDistrito
from app_user.models import User


def generar_reporte(request):
    user: User = request.user
    distrito = user.distrito
    if not distrito:
        messages.error(request, 'Este usuario no tiene un Distrito asociado.')
        return redirect('/admin/app_main/distrito/')
    if distrito.evaluado:
        messages.error(request, 'El Distrito ya está evaluado, debe crear nuevos Presbiterios.')
        return redirect('/admin/app_main/distrito/')

    attrs = list(distrito.__dict__.keys())[2:]
    resumen = ResumenDistrito()
    for a in attrs:
        setattr(resumen, a, getattr(distrito, a))

    resumen.cantidad_meses = int(request.POST['meses'])
    resumen.user = user
    resumen.save()

    users = distrito.user_set.all()
    for user in users:
        for presb in user.presbiterio_set.all():
            presb.evaluado = True
            presb.save()

    for a in attrs:
        if a not in ['nombre', 'apellidos', 'distrito', 'fecha', 'evaluado']:
            setattr(distrito, a, 0)
    distrito.evaluado = True
    distrito.save()

    messages.success(request, f'Se creó un resumen de {request.POST["meses"]} meses. Los valores del Distrito '
                              f'se reiniciaron.')
    return redirect('/admin/app_main/resumendistrito/')
