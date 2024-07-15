from django.urls import path
from .views import ListaPendientes, NumerosTelefonosLista, DetalleTarea, DetalleNumerosTelefonos, CrearTarea,CrearNumeroTelefono,EditarTarea,EliminarTarea,EditarNumeroTelefono,EliminarNumeroTelefono,Logueo,Registrar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # REGISTRARSE
    path('registrar/', Registrar.as_view(), name='registro'),
    # LOGIN / LOGUT
    path('login/', Logueo.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # TAREAS
    path('', ListaPendientes.as_view(), name='tareas'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea'),
    # Numeros Telefonos
    path('numeros/', NumerosTelefonosLista.as_view(), name='numeros-telefonos-lista'),
    path('numeros/<int:pk>', DetalleNumerosTelefonos.as_view(), name='detalle-numero-telefonico'),
    path('crear-numero-telefono', CrearNumeroTelefono.as_view(), name='crear-numero-telefonico'),
    path('editar-numeros/<int:pk>', EditarNumeroTelefono.as_view(), name='editar-numeros'),
    path('eliminar-numero/<int:pk>', EliminarNumeroTelefono.as_view(), name='eliminar-numero'),

]
