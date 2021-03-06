from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),    
    url(r'^$', 'empleados.views.index', name='index'),	
	url(r'^login/$', 'empleados.views.LoginView', name='login'),
    url(r'^logout/$', 'empleados.views.LogoutView', name='logout'),  
    url(r'^empleados/', include('empleados.urls')),   
)

handler404 = 'productos.views.file_not_found_404' 
if settings.DEBUG == False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
   )