from django.db import models

# Create your models here.
class secret_intro( models.Model ):

    text = models.CharField( max_length = 20 )