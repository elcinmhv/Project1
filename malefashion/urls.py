"""
URL configuration for malefashion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core.urls import urlpatterns as core_urls
from user.urls import urlpatterns as user_urls
from core.api.urls import urlpatterns as core_api_urls
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include(core_urls)),
    
    
]


urlpatterns += i18n_patterns(
     path('admin/', admin.site.urls),
     path('',include(core_urls)),
     path('',include(user_urls)),
     path('api-auth/',include('rest_framework.urls')),
     path('api/',include(core_api_urls)),
     path('', include('social_django.urls', namespace='social')),
    #  path('i18n/',include('django.conf.urls.i18n'))

)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/',include('rosetta.urls'))
    ]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)