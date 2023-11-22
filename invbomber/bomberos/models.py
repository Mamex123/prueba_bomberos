from django.db import models

class Articulos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name = "Nombre")
    descripcion = models.CharField(max_length=250, verbose_name="Descripcion", null=True)
    imagen = models.ImageField(upload_to='imagenes/',  verbose_name="imagen", null=True)

    def __str__(self):

        fila = "Nombre: " + self.nombre + "-" + "Descripcion: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
