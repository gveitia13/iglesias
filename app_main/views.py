from django.contrib import messages
from django.shortcuts import redirect

from app_main.models import ResumenDistrito
from app_user.models import User


def generar_reporte(request):
    print(request.POST['meses'])
    user: User = request.user
    distrito = user.distrito
    if not distrito:
        messages.error(request, 'Este usuario no tiene un Distrito asociado')
        return redirect('/admin/app_main/distrito/')

    attrs = list(distrito.__dict__.keys())[2:]
    resumen = ResumenDistrito()
    for a in attrs:
        setattr(resumen, a, getattr(distrito, a))
    resumen.cantidad_meses = int(request.POST['meses'])
    resumen.save()
    return redirect('/admin/app_main/resumendistrito/')
