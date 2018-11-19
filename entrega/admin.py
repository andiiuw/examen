from django.contrib import admin

from .models import (Sala)
from .models import (Ciudad,CiudadAdmin)
from .models import Pelicula
from .models import Paquete

admin.site.register(Sala)
admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Pelicula)
admin.site.register(Paquete)
# Register your models here.
