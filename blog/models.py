from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="Títol")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación") #al atribut es guarda la data de creacio del objecte de manera automatica
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición") #al atribut es guarda la data de la ultima modificacio del object

    class Meta:
        verbose_name="categoría"
        verbose_name_plural="categorías" #si no especifiquem aquesta variable, per defecte afegeix una S al nom definit (per defecte o al verbose_name)
        ordering=["-created"] # posem un guio - per indicar que el ordre ha de ser a la inversa, en aquest cas no volem que sigui del registre mes antic al mes nou sino al contrari, del mes nou al mes antic

    def __str__(self):
        return(self.name)

class Post(models.Model):
    title=models.CharField(max_length=200,verbose_name="Título")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de Publicación",default=now)
    image=models.ImageField(verbose_name="Imagen",upload_to="blog")
    author=models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category,verbose_name="Categorias",related_name="get_posts")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación") #al atribut es guarda la data de creacio del objecte de manera automatica
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición") #al atribut es guarda la data de la ultima modificacio del object

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas" #si no especifiquem aquesta variable, per defecte afegeix una S al nom definit (per defecte o al verbose_name)
        ordering=["-created"] # posem un guio - per indicar que el ordre ha de ser a la inversa, en aquest cas no volem que sigui del registre mes antic al mes nou sino al contrari, del mes nou al mes antic

    def __str__(self):
        return(self.title)
