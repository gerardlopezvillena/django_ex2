from django.db import models

# Create your models here.
class Link(models.Model):
    key=models.SlugField(verbose_name="Nombre Clave",max_length=100,unique=True)
    name=models.CharField(verbose_name="Red Social",max_length=200)
    url=models.URLField(verbose_name="Enlace",max_length=200,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación") #al atribut es guarda la data de creacio del objecte de manera automatica
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición") #al atribut es guarda la data de la ultima modificacio del object

    class Meta:
        verbose_name="enlace"
        verbose_name_plural="enlaces" #si no especifiquem aquesta variable, per defecte afegeix una S al nom definit (per defecte o al verbose_name)
        ordering=["name"] # posem un guio - per indicar que el ordre ha de ser a la inversa, en aquest cas no volem que sigui del registre mes antic al mes nou sino al contrari, del mes nou al mes antic

    def __str__(self):
        return(self.name)


