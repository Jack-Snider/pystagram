from django.db import models

# Create your models here.
class Sender( models.Model ):

    message = models.CharField( max_length = 20 )

    def __str__( self ):
        return f'{ self.pk } : { self.message }'
