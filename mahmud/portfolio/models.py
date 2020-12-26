from django.db import models
import datetime

class post(models.Model):
	Title = models.CharField(max_length=100)
	Sub_title = models.CharField(max_length=100, blank=True)
	Text = models.TextField()
	Image = models.ImageField(upload_to='images/')
	Link=models.URLField('Web Address', blank=True)
	Date = models.DateField(default=datetime.date.today)
	
	class Meta:
		verbose_name_plural = "Post"

	def __str__(self):
		return self.Title

