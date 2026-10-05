from django.db import models

# Create your models here.

class FotoGaleria(models.Model):
    imagen = models.ImageField(upload_to="galeria/")
    descripcion = models.CharField(max_length=200, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return self.descripcion or f"Fodo {self.id}"

        