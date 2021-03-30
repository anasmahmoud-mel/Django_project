from import_export import resources
from .models import Person
from .models import Activity

class PersonResource(resources.ModelResource):
    class meta:
        model = Person

class ActivityResource(resources.ModelResource):
     class Meta:
          model = Activity