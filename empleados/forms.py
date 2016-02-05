#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from PIL import Image
from .models import Empleado,Archivo,Periodo_Vacaional

class empleadoForm(ModelForm):

	class Meta:
		model = Empleado
		fields = ('direccion',)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')

class ContrasenaForm(ModelForm):
    class Meta:
        model = User
        fields = ('password',)

class GeneralesForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name',)

class empleadoFullForm(ModelForm):

	class Meta:
		model = Empleado
		fields = ('user','direccion','telefono','celular','departamento','puesto','imagen')

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')

class archivoForm(ModelForm):
	class Meta:
		model = Archivo
		fields = '__all__'

class DatosEmpresarialesForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ('fecha_ingreso','departamento','puesto','salario_contratacion','salario_actual','tipo_contrato')

class DatosPersonalesForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ('edad','estado_civil','escolaridad','direccion','telefono','celular','curp','rfc','numero_seguridad_social',)

class PeriodoVcacionalForm(ModelForm):
	class Meta:
		model = Periodo_Vacaional
		fields = '__all__'

