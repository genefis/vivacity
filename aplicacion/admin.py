from django.contrib import admin
from .models import eventos
from .models import hospedaje
from .models import lugares
from .models import canton
admin.site.register(eventos)#, #eventosAdmin)
admin.site.register(hospedaje)#, #eventosAdmin)
admin.site.register(lugares)#, #eventosAdmin)
admin.site.register(canton)#, #eventosAdmin)
# Register your models here.
