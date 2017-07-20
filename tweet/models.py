from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Twitt(models.Model):
    text = models.CharField(max_length=250, null=False)
    date_twit = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    user_twit = models.ForeignKey(User,
                                  null=False,
                                  blank=False,
                                  on_delete=models.CASCADE,
    )

    def __str__(self):
        return ('{} {}'.format(self.user_twit,self.text))

    #Especificando campo por el cual se ordenara la informacion
    class Meta:
        ordering = ["-date_twit"]
