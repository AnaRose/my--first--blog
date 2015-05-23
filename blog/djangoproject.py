from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_lenght=200)
	text = models.TextField()
	Created_date = models.DateTimeField(default=timezone.now)
	publised_date = models.DateTimeField(blank=True, null=True)

		def  publish(self):
			self.publised_date = timezone.now()
			self.save()
			pass
# Create your models here.
