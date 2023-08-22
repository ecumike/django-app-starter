from django.urls import include, path, re_path

from core.views import signin, signout

urlpatterns = [
	## Sign in/out.
	path('signin/', signin, name='signin'),
	path('signout/', signout, name='signout'),

]


