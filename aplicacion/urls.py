
from django.urls import path
from django.contrib.auth.decorators import login_required
# se importa las vistas de la aplicación
from django.contrib.auth.views import logout_then_login
from . import views


urlpatterns = [
    
    path('',views.index,name='index'),
    path('accounts/login/',views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('eventos/',login_required(views.eventos),name='eventos'),
    path('tour/',views.tour,name='tour'),
    path('hospedaje/',login_required(views.hospedaje),name='hospedaje'),
    path('lugares/',login_required(views.lugares),name='lugares'),
    path('logout/',logout_then_login,name='logout'),
    path('salir/',views.salir,name='salir'),
    path('listarCanton/',views.listarCanton,name='listarCanton'),
    path('listarEventosPorCanton/',views.listarEventosPorCanton,name='listarEventosPorCanton')


]
         
