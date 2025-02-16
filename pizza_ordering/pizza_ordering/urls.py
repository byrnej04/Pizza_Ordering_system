from django.contrib import admin
from django.urls import path, include
from pizza_app.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', custom_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pizza_app.urls'))
]

