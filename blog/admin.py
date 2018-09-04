from django.contrib import admin
from .models import Category,Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    list_display=('title','author','published','post_categories')
    ordering=('author','published')
    search_fields=('title','content','author__username','categories__name')
    date_hierarchy='published'
    list_filter=('author__username','categories__name')

    def post_categories(self,obj): #obj fa referencia a cada objecte (sembla una paraula reservada)
        return(", ".join([c.name for c in obj.categories.all().order_by('name')])) #com que lobjecte #al metode post_categories li crido del objecte creat, selecciono les categories (que ja les tinc importades per a Registra el model Category), i d'aquestes selecciono totes les instancies amb all() 

    post_categories.short_description="Categorías"

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
