from django.shortcuts import redirect


def generar_reporte(request):
    print(request.POST['meses'])
    return redirect('/admin/app_main/distrito/')
