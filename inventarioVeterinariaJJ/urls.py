"""
URL configuration for inventarioVeterinariaJJ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from gestorProductos.views import *
from gestorProductos import views


from gestorUser.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestor/', include('gestorUser.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", index, name="home"),
    path("", include("gestorUser.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"  ),
    path('gestionar/', gestionar_productos, name='gestionar_productos'),  # Redirección según usuario
    path("productosAdmin/", views.inventarioAdmin, name='productosAdmin'), #vista para productos desde superuser
    path('', views.lista_productos, name='lista_productos'),
    path('productosAdmin/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productosAdmin/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('productosAdmin/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productosUsuario/', TemplateView.as_view(template_name="productosUsuario.html"), name='productosUsuario'),  # Vista para usuarios normales
    path('productos/agregar/', views.agregar_producto, name='agregar_producto_usuario'),
    path('productos/editar/<int:producto_id>/', views.editar_producto_usuario, name='editar_producto_usuario'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto_usuario, name='eliminar_producto_usuario'),
]
