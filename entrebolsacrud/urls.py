from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('interfaz/', views.interfaz,name='interfaz'),
    path('agregarProd/', views.agregarProd),
    path('eliminarProd/', views.eliminarProd),
    path('editarProd/', views.editarProd),
    path('confirmarEdit/', views.confirmarEdit),
    path('eliminar/<clave>', views.eliminar),
    path('login/',LoginView.as_view(template_name='core/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='core/login.html'),name='logout'),
    path('admin/', admin.site.urls),
    path('interfaz/eliminar1/<codigo>', views.eliminar1),
    path('interfaz/modificar1/<codigo>', views.modificar1),
    path('search/',views.search,name='search'),
    path('comparar/<nombre>/<codigo>',views.comparar,name='comparar'),
    path('comparison/',views.comparison,name='comparison')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)