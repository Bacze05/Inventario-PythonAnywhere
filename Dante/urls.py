#TENEMOS QUE REVISAR LAS URLS , ACTUALIZARLAS PORQUE SE INCORPORO USERS 
#TENEMOS QUE CREAR ARCHIVOS URLS.PY EN CADA APP PARA QUE SEAN AUN MAS INDEPENDIENTE Y MAS CLEAN CODE ACA
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.views import logout_then_login,redirect_to_login
from django.conf.urls.static import static
import users.views as users1
from Venta import views as venta
import Inventario.views as Inventario
from inventarioApi import views as Api

urlpatterns = [
    #LOGIN
    path('', Inventario.Home.as_view(), name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inventario/', include('Inventario.urls')),
    path('user/', include('users.urls')),
    path('api/', include('inventarioApi.urls')),
    path('venta/', include('Venta.urls')),
    path('admin/', admin.site.urls),

]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    

    
    
   
    
   
    