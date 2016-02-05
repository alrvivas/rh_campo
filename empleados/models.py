from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Departamento(models.Model):
	nombre 	= models.CharField(max_length=140)
	descripcion = models.TextField()

	def __unicode__(self): 
		return unicode(self.nombre)

class Puesto(models.Model):
	nombre = models.CharField(max_length=140)
	departamento = models.ForeignKey(Departamento,null=True)
	perfil = models.TextField()
	salario_minimo_inicial = models.PositiveIntegerField(null=True)
	salario_maximo_inicial = models.PositiveIntegerField(null=True)

	def __unicode__(self): 
		return unicode(self.nombre)

class Contrato(models.Model):
	nombre = models.CharField(max_length=140)

	def __unicode__(self): 
		return unicode(self.nombre)


class Empleado(models.Model):
	user = models.OneToOneField(User,null=True, blank=True)
	fecha_ingreso = models.DateField(null=True)
	direccion = models.CharField(max_length=140,null=True)
	curp = models.CharField(max_length=20,null=True)
	rfc = models.CharField(max_length=20,null=True)
	numero_seguridad_social = models.CharField(max_length=12,null=True)
	celular	= models.CharField(max_length=15,null=True)
	telefono = models.CharField(max_length=15,null=True)
	edad = models.PositiveIntegerField(null=True)
	estado_civil = models.CharField(max_length=150,null=True)
	escolaridad = models.CharField(max_length=50,null=True)
	preparacion_academica = models.CharField(max_length=140,null=True)	
	departamento = models.ForeignKey(Departamento,null=True,)
	puesto = models.ForeignKey(Puesto,null=True,)
	tipo_contrato = models.ForeignKey(Contrato,null=True)
	salario_contratacion = models.PositiveIntegerField(null=True)
	salario_actual = models.PositiveIntegerField(null=True)
	imagen = models.ImageField("Imagen Categoria", upload_to="images/categorias", blank=True, null=True)
	
	@models.permalink
	def get_absolute_url(self):
		return('empleado', (), { 'empleado_id': self.id })

	@models.permalink
	def get_absolute_url_add(self):
		return('add-empleado', (), { 'empleado_id': self.id })

	@models.permalink
	def get_absolute_url_editar(self):
		return('editar-empleado', (), { 'empleado_id': self.id })

	@models.permalink
	def get_absolute_url_editar_empresariales(self):
		return('editar-empresariales', (), { 'empleado_id': self.id })



	def __unicode__(self):
		return unicode(self.id)

class Archivo(models.Model):
	empleado = models.ForeignKey(Empleado)
	nombre = models.CharField(max_length=140)
	archivo = models.FileField("Archivos", upload_to="archivos/categorias", blank=True, null=True)

	def __unicode__(self):
		return unicode(self.id)

class Actas_Administrativas(models.Model):
	empleado = models.ForeignKey(Empleado)
	descripcion = models.TextField()
	archivo = models.FileField("Acta Administrativa", upload_to="archivos/categorias", blank=True, null=True)

	def __unicode__(self):
		return unicode(self.id)

class Periodo_Vacaional(models.Model):
	empleado = models.ForeignKey(Empleado)
	titulo = models.CharField(max_length=80,null=True)
	descripcion = models.TextField(null=True)
	fecha_inicio = models.DateField(null=True)
	fecha_fin = models.DateField(null=True)


	def __unicode__(self):
		return unicode(self.id)

	@models.permalink
	def get_absolute_url(self):
		return('periodo-vacacional', (), { 'vacaciones_id': self.id })

	@models.permalink
	def get_absolute_url_editar(self):
		return('editar-periodo-vacacional', (), { 'vacaciones_id': self.id })