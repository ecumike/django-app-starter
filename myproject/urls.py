"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

from core.views import signin, signout


# This is if you want to do custom processing for a 404/500.
# (log errors and send email/slack messages)
# Otherwise just make 403/404/500.html template file.
handler403 = 'core.views.custom_403'
handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'

urlpatterns = [
	path('djangoadmin/doc/', include('django.contrib.admindocs.urls')),
	path('djangoadmin/', admin.site.urls),
	path('hijack/', include('hijack.urls')),
	path("__debug__/", include("debug_toolbar.urls")),
	
	## Map default favicon URL to static file location.
	re_path(r'^favicon.ico$', RedirectView.as_view(
		url=staticfiles_storage.url('favicon.ico'),
		permanent=False),
		name="favicon"
	),
	
	path('', RedirectView.as_view(pattern_name='myapp:home', permanent=False)),
	path('', include(('core.urls', 'core'))),
	path('myapp/', include(('myapp.urls', 'myapp'))),
	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


