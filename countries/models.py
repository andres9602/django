from django.db import models


class ActiveManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(active=True)

class Country(models.Model):
	CODES_CHOICES	= (
		('colombia', 'CO'),
		('estados unidos', 'US'),
		('mexico', 'MX'),
		('argentina', 'AR'),
	)

	name = models.CharField(max_length=255)
	code = models.CharField(max_length=3, choices=CODES_CHOICES)
	continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)
	active = models.BooleanField(default=True)
	active_manager = ActiveManager()
	objects = models.Manager()

	def __str__(self):
		return self.name
