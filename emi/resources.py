
from import_export import resources
from .models import Students

class EtudiantResource(resources.ModelResource):
    class Meta:
        model = Students


