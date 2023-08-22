import sys

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from core.models import *


##
##	/signin/
##
def signin(request):
	"""
	Sign in page
	"""
	response = render(request, 'core/signin.html', {
		'form': AuthenticationForm,
	})
	
	## If user is already signed in they don't need to be here, so redirect them to home page.
	if request.user.is_authenticated:
		response = redirect(request.GET.get('next', reverse('myapp:home')))
	
	elif request.method == 'GET':
		response = render(request, 'core/signin.html', {
			'form': AuthenticationForm,
		})
		
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		# NOTE: This ensures all usernames/emails to be lowercase. Prevents mismatch
		# for users with mix-case emails.
		try:
			user = authenticate(request, username=username.lower(), password=password)
		except Exception as ex:
			context = {
				'form': AuthenticationForm,
				'error': 'Uh oh, we were unable to authenticate you. Check your ID/PW and try again.',
			}
			
			return render(request, 'core/signin.html', context)
		
		## Success
		if user is not None:
			login(request, user)
			
			# Hit some company profile API to create/update their profile.
			#updateUserProfile(user)
			
			# Send them back to the page they originally went to before they had to sign in.
			response = redirect(request.POST.get('next', reverse('myapp:home')))
			
		## Fail
		else:
			context = {
				'form': AuthenticationForm,
				'error': 'Hmm, it seems your ID/PW combination wasn\'t quite right.<br>Please try again.',
			}
			response = render(request, 'core/signin.html', context)
	
	return response
	

##
##	/signout/
##
def signout(request):
	"""
	Signs the user out.
	"""
	logout(request)
	return render(request, 'core/signout.html', {})


##
##	403
##
def custom_403(request, exception):
	"""
	This is only needed if you want to do custom processing when a 404 happens.
	"""
	error = ErrorLog.objects.create(
		user = request.user if not request.user.is_anonymous else None,
		url = request.get_full_path(),
		referer = request.META.get('HTTP_REFERER', 'None'),
		error_code = 403,
		error_message = 'Access denied',
	)
	
	error.sendSlackAlert()
		
	return render(request, 'core/403.html', {}, status=403)
	

##
##	404
##
def custom_404(request, exception):
	"""
	This is only needed if you want to do custom processing when a 404 happens.
	"""
	referer = request.META.get('HTTP_REFERER', 'None')
	
	if request.get_host() in referer:
		error = ErrorLog.objects.create(
			user = request.user if not request.user.is_anonymous else None,
			url = request.get_full_path(),
			referer = referer,
			error_code = 404,
			error_message = 'Page not found',
		)
		
		error.sendSlackAlert()
		
	return render(request, 'core/404.html', {}, status=404)
	

##
##	500
##
def custom_500(request):
	"""
	This is only needed if you want to do custom processing when a 500 happens.
	"""
	exc_info = sys.exc_info()
	errorTitle = exc_info[:2]
	errMsg = str(errorTitle or '(No error provided)')
	
	error = ErrorLog.objects.create(
		user = request.user if not request.user.is_anonymous else None,
		url = request.get_full_path(),
		referer = request.META.get('HTTP_REFERER', 'None'),
		error_code = 500,
		error_message = errMsg,
	)
	
	error.sendSlackAlert()
		
	return render(request, 'core/500.html', {}, status=500)
	

	
