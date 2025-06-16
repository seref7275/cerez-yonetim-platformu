from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/widgets/', include('widgets.urls')),
    path('csrf/', ensure_csrf_cookie(TemplateView.as_view(template_name='csrf.html')), name='csrf'),
]