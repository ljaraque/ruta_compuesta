from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from django.utils.http import urlencode
from django.shortcuts import redirect, render



class ProductosView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'autoriza/main.html')
        loginurl = reverse('login') + '?' + urlencode({'next': request.path})
        return redirect(loginurl)

class InicioView(View):
    pass

class EmpresaView(View):
    pass

class EquipoView(View):
    pass


class DumpPython(View):
    def get(self, req):
        response = "<pre>\nDatos de Usuario en Python:\n\n"
        response += "URL de Login: " + reverse('login') + "\n"
        response += "URL Logout: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            response += "User: " + req.user.username + "\n"
            response += "Email: " + req.user.email + "\n"
        else:
            response += "User is not logged in\n"

        response += "\n"
        response += "</pre>\n"
        response += """<a href="/autoriza">Go back</a>"""
        return HttpResponse(response)
    