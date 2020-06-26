from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('restapi/',include('restapi.urls')),
    path('api/v1/accounts/',include('rest_registration.api.urls'))
]
