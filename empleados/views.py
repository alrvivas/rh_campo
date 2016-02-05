# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Avg,Sum
from django.views.generic.base import View
from models import *
from forms import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  


@login_required(login_url='/login/')
def index(request):
    page_title = "Punto de Venta"
    user = request.user    
    template_name ="index.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

#@login_required(login_url='/login/')
def add_user(request):
    page_title = "Añadir Empleado Paso 1"
    last_user = User.objects.latest('id')
    empleado = Empleado.objects.all()
    if request.method == "POST":
        form_empleado = empleadoForm(request.POST)
        form = UserForm(request.POST)
        if form_empleado.is_valid() and form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            empleado = form_empleado.save(commit = False)
            empleado.save()
            return redirect(empleado.get_absolute_url_add())
    else:
        form_empleado = empleadoForm()
        form = UserForm() 
    template_name ="add-user.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def add_empleado(request,empleado_id):
    page_title = "Añadir Empleado Paso 2"
    user = request.user
    last_user = User.objects.latest('id')
    empleado = get_object_or_404(Empleado, id=empleado_id)
    vacaciones = Periodo_Vacaional.objects.all()
    departamentos = Departamento.objects.all()
    puestos = Puesto.objects.all()
    if request.method == 'POST':
        form_empleado = empleadoFullForm(request.POST,request.FILES, instance=empleado)
        form_vacaciones = PeriodoVcacionalForm(request.POST)
        if form_empleado.is_valid() and form_vacaciones.is_valid():
            empleado = form_empleado.save(commit = False)
            empleado.save() 
            vacaciones = form_vacaciones.save(commit = False)
            vacaciones.save()            
            return redirect(empleado.get_absolute_url())
    else:
        form_empleado = empleadoFullForm()
        form_vacaciones = PeriodoVcacionalForm()
    args = {}
    args.update(csrf(request))
    template_name ="add-empleado.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def empleados(request):
    page_title = "Empleados"
    user = request.user
    users = User.objects.all()
    empleados = Empleado.objects.filter(user=users)    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(user=query) 
        )    
        results = Empleado.objects.filter(qset).order_by('-id')
        template_name = "empleados-resultado.html"
        return render_to_response(template_name, {"results": results,"query": query,'page_title':page_title},context_instance=RequestContext(request)) 
    else:
        results = []        
    template_name ="empleados.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def empleado(request,empleado_id):
    user = request.user
    empleado = get_object_or_404(Empleado, id=empleado_id)
    vacaciones = Periodo_Vacaional.objects.filter(empleado=empleado).order_by('-id')
    periodo_vacaional = Periodo_Vacaional.objects.filter(empleado=empleado)
    vacacion = Periodo_Vacaional.objects.all()
    page_title = empleado.user
    user = request.user
    archivos = Archivo.objects.filter(empleado=empleado)
    archivo = Archivo.objects.all()
    if request.method == 'POST':
        form_archivo = archivoForm(request.POST,request.FILES)
        periodo_vacaional_form = PeriodoVcacionalForm(request.POST)
        if form_archivo.is_valid():
            archivo = form_archivo.save(commit = False)            
            archivo.save()
            return redirect(empleado.get_absolute_url())
        if periodo_vacaional_form.is_valid():
            vacacion = periodo_vacaional_form.save(commit = False)            
            vacacion.save()
            return redirect(vacacion.get_absolute_url())
    else:
        form_archivo = archivoForm()
        periodo_vacaional_form = PeriodoVcacionalForm()
    args = {}
    args.update(csrf(request))   
    template_name ="empleado.html" 
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editar_empleado(request,empleado_id):
    page_title = "Editar Datos Persoanles"
    user = request.user
    empleado = get_object_or_404(Empleado,id=empleado_id)
    periodo_vacaional = Periodo_Vacaional.objects.filter(empleado=empleado)
    if request.method == 'POST':
        form_empleado = DatosPersonalesForm(request.POST,instance=empleado)
        if form_empleado.is_valid():
            empleado = form_empleado.save(commit = False)        
            empleado.save() 
            return redirect(empleado.get_absolute_url())
    else:
        form_empleado = DatosPersonalesForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-empleado.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def editar_empresariales(request,empleado_id):
    page_title = "Editar Datos Empresariales"
    user = request.user
    empleado = get_object_or_404(Empleado, id=empleado_id)
    periodo_vacaional = Periodo_Vacaional.objects.filter(empleado=empleado)
    departamentos = Departamento.objects.all()
    tipo_contrato = Contrato.objects.all()
    puestos = Puesto.objects.all()
    if request.method == 'POST':
        empleado_form = DatosEmpresarialesForm(request.POST,instance=empleado)
        if empleado_form.is_valid():
            empleado = empleado_form.save(commit = False)          
            empleado.save()  
            return redirect(empleado.get_absolute_url())
    else:
        empleado_form = DatosEmpresarialesForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-empresariales.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request)) 


@login_required(login_url='/login/')
def periodo_vacacional(request,vacaciones_id):
    page_title = "Asinar Periodo Vacacional"
    user = request.user
    periodo_vacaional = get_object_or_404(Periodo_Vacaional, id=vacaciones_id)
    puestos = Puesto.objects.all()
    if request.method == 'POST':
        vacaiones_form = PeriodoVcacionalForm(request.POST,instance=periodo_vacaional)
        if vacaiones_form.is_valid():
            periodo_vacaional = vacaiones_form.save(commit = False)          
            periodo_vacaional.save()  
            return redirect(periodo_vacaional.empleado.get_absolute_url())
    else:
        vacaiones_form = PeriodoVcacionalForm()
    args = {}
    args.update(csrf(request))
    template_name ="asignar-periodo-vacacional.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editar_periodo_vacacional(request,vacaciones_id):
    page_title = "Editar Periodo Vacacional"
    user = request.user
    periodo_vacaional = get_object_or_404(Periodo_Vacaional, id=vacaciones_id)
    if request.method == 'POST':
        vacaiones_form = PeriodoVcacionalForm(request.POST,instance=periodo_vacaional)
        if vacaiones_form.is_valid():
            periodo_vacaional = vacaiones_form.save(commit = False)          
            periodo_vacaional.save()  
            return redirect(periodo_vacaional.empleado.get_absolute_url())
    else:
        vacaiones_form = PeriodoVcacionalForm()
    args = {}
    args.update(csrf(request))
    template_name ="editar-periodo-vacacional.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def periodo_vacacional(request,vacaciones_id):
    page_title = "Asignar Periodo Vacacional"
    user = request.user
    periodo_vacaional = get_object_or_404(Periodo_Vacaional, id=vacaciones_id)
    if request.method == 'POST':
        vacaiones_form = PeriodoVcacionalForm(request.POST,instance=periodo_vacaional)
        if vacaiones_form.is_valid():
            periodo_vacaional = vacaiones_form.save(commit = False)          
            periodo_vacaional.save()  
            return redirect(periodo_vacaional.empleado.get_absolute_url())
    else:
        vacaiones_form = PeriodoVcacionalForm()
    args = {}
    args.update(csrf(request))
    template_name ="asignar-periodo-vacacional.html"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request)) 


