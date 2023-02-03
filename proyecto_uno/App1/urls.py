from django.urls import path
from App1.views import *

urlpatterns = [
    #PAGINAS DE  INICIO DE CADA MODELO
    path('', inicio, name= "inicio"),
    path('recCarne/', vrecCarne, name= "recCarne"),
    path('recVerduras/', vrecVerduras, name= "recVerduras"),
    path('recPastas/', vrecPastas, name="recPastas"),
    path('contacto/', vcontacto, name= "contacto"),
    #PAGINA DE REGISTRO EXITOSO
    path('regExitoso/', vregExitoso, name= "registroExitoso"),
    #PAGINAS DE FORMULARIOS DE CARGA DE DATOS
    path('formRecCarne/', recCarneForm, name= "registroRecCarne" ),
    path('formRecVerduras/', recVerduraForm, name="registroRecVerduras" ),
    path('formRecPastas/', recPastasForm, name="registroRecPastas"),
    path('formContacto/', ContactoForm, name="registroContacto"  ),
    #PAGINAS DE FORMULARIO DE BUSQUEDA
    path('busquedaCarne/', busquedaCarnes, name="busquedaCarnes" ),
    path('busquedaVerduras/', busquedaVerduras, name="busquedaVerduras" ),
    path('busquedaPastas/', busquedaPastas, name="busquedaPastas" ),

    #PAGINAS DE RESULTADOS
    path('resultadoCarne/', resultadosCarnes, name="resultadosCarnes" ),
    path('resultadoVerduras/', resultadosVerduras, name="resultadosVerduras" ),
    path('resultadoPastas/', resultadosPastas, name="resultadosPastas" ),

]
