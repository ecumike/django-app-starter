import requests

from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class ErrorLog(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	
	user = models.ForeignKey(User, related_name='error_log_user', null=True, on_delete=models.SET_NULL)
	url = models.CharField(max_length=300)
	referer = models.CharField(max_length=300, null=True)
	error_code = models.PositiveIntegerField(default=0)
	error_message = models.TextField()

	class Meta:
		ordering = ['-created_at']
		
	def __str__(self):
		return f'{self.created_at} - {self.error_message}'

	
	def sendSlackAlert(self):
		"""
		Use saved error push a message to the Slack web hook URL for your room.
		"""
		slackUrl = settings.SLACK_ALERT_URL
		
		if slackUrl:
			icon = ':error:' if errorCode > 499 else ':warning:'
		
			user_name = self.user.username if self.user else 'N/A'
				
			payload = {
				'username': 'Myproject',
				'icon_emoji': icon,
				'text': f'*A {self.error_code} error just happened*\n*Requested path:*  {self.url}\n*Referring page:*  {self.referer}\n*User:*  {user_name}\n*Error:*  {self.error_message}',
			}
			
			r = requests.post(slackUrl, json=payload)
		
