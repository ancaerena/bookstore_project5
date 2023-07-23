from django.forms import ModelForm
from .models import *
 
class CreateInSubject(ModelForm):
    class Meta:
        model= Subject
        fields = "__all__"
 
class CreateInComments(ModelForm):
    class Meta:
        model= Comments
        fields = "__all__"