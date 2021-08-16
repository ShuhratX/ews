from django.db import models
from django.contrib.auth. models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class TrainingCenters(AbstractUser):
	username = None
	email = models.EmailField(_('email address'), unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	name = models.CharField(max_length=50, verbose_name='name')
	photo = models.ImageField()
	text = models.TextField()
	phone_number = models.CharField(max_length=50)
	telegram = models.CharField(max_length=100, blank=True)
	instagram = models.CharField(max_length=100, blank=True)
	you_tube = models.CharField(max_length=100, blank=True)
	LANGUAGE = (
		('uz', 'uz'),
		('ru', 'ru'),
		('en', 'en')
		)
	languages = models.CharField(max_length=10, choices=LANGUAGE)
	msg = models.CharField(max_length=10, null=True, blank=True)
	verified = models.BooleanField(default=False)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "O'quv markaz"
		verbose_name_plural = "O'quv markazlar"