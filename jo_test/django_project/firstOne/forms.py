from django import forms
from .models import Person
from .models import Activity
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class ActivityForm(forms.ModelForm):
     class Meta:
         model = Activity
         fields = '__all__'