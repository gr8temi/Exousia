from django.contrib import admin

# Register your models here.
from .models import categories,size,brand,gender,Product,States,Lga
from import_export.admin import ImportExportModelAdmin

class ViewAdmin(ImportExportModelAdmin):
	pass


admin.site.register(categories)
admin.site.register(size)
admin.site.register(brand)
admin.site.register(gender)
admin.site.register(Product)
admin.site.register(States, ViewAdmin)
admin.site.register(Lga, ViewAdmin)

