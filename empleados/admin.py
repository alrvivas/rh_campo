from django.contrib import admin
from .models import Departamento,Puesto,Empleado, Archivo,Actas_Administrativas,Contrato,Periodo_Vacaional

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
	list_display 	= ('id','archivo',)

@admin.register(Actas_Administrativas)
class Actas_AdministrativasAdmin(admin.ModelAdmin):
	list_display 	= ('id','empleado',)

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Periodo_Vacaional)
class Periodo_VacaionalAdmin(admin.ModelAdmin):
	list_display 	= ('id','empleado','fecha_inicio','fecha_fin')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('id','user','puesto',)
	list_editable = ('puesto',)
	list_filter = ('puesto',)
	search_fields = ('user','puesto',)
