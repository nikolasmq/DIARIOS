from django.db import models

# Create your models here.

class ModeloGeneral(models.Model):
    order = models.PositiveIntegerField('Orden')
    created = models.DateTimeField('Fecha de cración', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        abstract = True

class TemasModel(ModeloGeneral):
    nombre_tema = models.CharField("Nombre del tema", max_length=100)
    descripcion_tema =  models.TextField("Descripción del tema")

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        db_table = "apps_temas"
        ordering = ['order']

    def __str__(self):
        return f"{self.id} - {self.nombre_tema} - {self.created} - {self.updated} "
    

class ContenidoModel(ModeloGeneral):
    nombre_unidad = models.CharField("Nombre de la Unidad", max_length=10050)
    competencia_a_desarrollar = models.TextField("Competencia a desarrollar")
    temas = models.ManyToManyField(TemasModel)

    class Meta:
        verbose_name = "Contenido"
        verbose_name_plural = "Contenidos"
        db_table = "apps_contenido"
        ordering = ['order']

    def __str__(self):
        return f"{self.id} - {self.nombre_unidad} - {self.created} - {self.updated}"


