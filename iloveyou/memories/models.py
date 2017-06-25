from django.db import models
from django.conf import settings


# Create your models here.
class Memory(models.Model):
    """
    Class to encapsulate my memories and love for Lucie


    Because she deserves cool memories and love
    Because she is awesome
    """
    name = models.CharField(verbose_name='Lovely Object Name', max_length=50, blank=True, null=True)
    picture = models.ImageField(upload_to=settings.MEDIA_ROOT+'/pictures', verbose_name='Lovely Photos', blank=True, null=True)
    sound = models.FileField(upload_to=settings.MEDIA_ROOT+'/sounds', verbose_name='Lovely Sounds', blank=True, null=True)
    text = models.TextField(verbose_name='Lovely Words', max_length=500, blank=True, null=True)
    picture_rotation = models.IntegerField(verbose_name='Lovely Rotation Angle', choices=[(0, '0 Degrees'),
                                                                                          (90, '90 Degrees'),
                                                                                          (180, '180 Degrees'),
                                                                                          (270, '270 Degrees')], blank=True, null=True, default=0)

    class Meta:
        """
        Fix the non-lovely admin panel
        """
        verbose_name_plural = "Memories"

    def __str__(self):
        """
        What the lovely memory is called in the admin panel
        :return:
        """
        return self.name
