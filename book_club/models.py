from django.db import models

from profiles.models import UserProfile

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200,default="anonymous" )
    email = models.CharField(max_length=200,null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    link = models.CharField(max_length=100 ,null =True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.topic)

class Comments(models.Model):
    class Meta:
        verbose_name_plural = 'Comments'

    subject = models.ForeignKey(Subject,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

 
    def __str__(self):
        # return str(self.subject)
        return str(self.discuss)