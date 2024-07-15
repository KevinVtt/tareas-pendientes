from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarea,NumerosTelefonicos

# REGISTRAR

class Registrar(FormView):
    template_name = 'base/registrarUsuario.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    def form_valid(self,form):
        usuario = form.save()
        if usuario is not None:
            login(self.request,usuario)
        return super(Registrar,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')

        return super(Registrar,self).get(*args, **kwargs)

# LOGIN

class Logueo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_field_name = True

    def get_success_url(self):
        return reverse_lazy('tareas')

# TAREA

class ListaPendientes(LoginRequiredMixin,ListView):
    model = Tarea
    context_object_name = 'tareas'
    template_name = 'base/tarea.html'

    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context

    

class DetalleTarea(LoginRequiredMixin,DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tareaDetalle.html'

class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tarea
    fields = ['titulo','descripcion','completo']
    success_url = reverse_lazy('tareas')

    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super(CrearTarea,self).form_valid(form)

class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin,DeleteView):
    model = Tarea
    context_object_name = 'tareas'
    success_url = reverse_lazy('tareas')
    template_name = 'base/eliminarTarea.html'

# Numeros Telefonos

class NumerosTelefonosLista(LoginRequiredMixin,ListView):
    model = NumerosTelefonicos
    context_object_name = 'numeros_telefonicos'
    template_name = 'base/numerosTelefono.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numeros_telefonicos'] = NumerosTelefonicos.objects.filter(usuario=self.request.user)
        return context



class DetalleNumerosTelefonos(LoginRequiredMixin,DetailView):
    model = NumerosTelefonicos
    context_object_name = 'numeros'
    template_name = 'base/numerosTelefonoDetalle.html'
    

class CrearNumeroTelefono(LoginRequiredMixin,CreateView):
    model = NumerosTelefonicos
    fields = ['numero_telefono','nacionalidad','fecha_nacimiento','numero_area']
    success_url = reverse_lazy('numeros-telefonos-lista')
    template_name = 'base/crearNumeroTelefono.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearNumeroTelefono, self).form_valid(form)


class EditarNumeroTelefono(LoginRequiredMixin,UpdateView):
    model = NumerosTelefonicos
    fields = '__all__'
    success_url = reverse_lazy('numeros-telefonos-lista')
    template_name = 'base/crearNumeroTelefono.html'

class EliminarNumeroTelefono(LoginRequiredMixin,DeleteView):
    model = NumerosTelefonicos
    context_object_name = 'numero-telefono'
    success_url = reverse_lazy('numeros-telefonos-lista')
    template_name = 'base/eliminarNumero.html'