from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^$', 'empleados.views.index', name='index'),
	url(r'^$', 'empleados.views.empleados', name='empleados'),	
	url(r'^perfil/(?P<empleado_id>[-\w]+)$', 'empleados.views.empleado', name='empleado'), 
	url(r'^add-user/$', 'empleados.views.add_user', name='add-user'),
	url(r'^add-empleado/(?P<empleado_id>[-\w]+)$', 'empleados.views.add_empleado', name='add-empleado'), 
	url(r'^editar-empleado/(?P<empleado_id>[-\w]+)$', 'empleados.views.editar_empleado', name='editar-empleado'),
	url(r'^editar-empresariales/(?P<empleado_id>[-\w]+)$', 'empleados.views.editar_empresariales', name='editar-empresariales'), 
	url(r'^editar-periodo-vacacional/(?P<vacaciones_id>[-\w]+)$', 'empleados.views.editar_periodo_vacacional', name='editar-periodo-vacacional'), 
	url(r'^periodo-vacacional/(?P<vacaciones_id>[-\w]+)$', 'empleados.views.periodo_vacacional', name='periodo-vacacional'), 
)