from django.contrib import admin

from .models import Technology,Product,Category,Set
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]

class TechnologyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Technology._meta.fields]

class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]

class SetAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Set._meta.fields]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Set, SetAdmin)