from django.db import models
# Create your models here.
class canton(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nombre_canton =models.CharField(max_length=225,null =True)
    class Meta:
      verbose_name='nombre_canton'
      verbose_name_plural='nombre_cantones'
      ordering= ['nombre_canton']
    def __str__(self):
      return self.nombre_canton

       
class lugares(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nombre_lugar =models.CharField(max_length=225,null =True)
    fotolugar = models.ImageField(null=True)
    direccionlugar=models.URLField(null=True)
    horario=models.DateTimeField(null=True)
    tipo_lugar=models.CharField(max_length=225,null =True)
    canton_id = models.ForeignKey(canton ,on_delete = models.CASCADE)
    class Meta:
        verbose_name='lugares'
        verbose_name_plural='lugares'
        ordering= ['nombre_lugar']
    def __str__(self):
      return self.nombre_lugar



class eventos(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nomEvento = models.CharField(max_length=225,null =True)
    fecha_inicio=models.DateTimeField(null=True)
    fecha_fin=models.DateTimeField(null=True)
    direccionEvento=models.URLField(null=True)
    infoEvento=models.TextField(max_length=225,null =True)
    fotoEvento = models.ImageField(null=True)
    canton_id = models.ForeignKey(canton, on_delete = models.CASCADE)
    class Meta:
        verbose_name='eventos'
        verbose_name_plural='eventos'
        ordering= ['nomEvento']
    def __str__(self):
      return self.nomEvento

class hospedaje(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nombre_hospedaje =models.CharField(max_length=225,null =True)
    fotoHospedaje = models.ImageField(null=True)
    direccionHospedaje=models.URLField(null=True)
    horario=models.CharField(max_length=225,null =True)
    tipoHospedaje=models.CharField(max_length=225,null =True)
    categoria=models.CharField(max_length=225,null =True)
    canton_id = models.ForeignKey(canton ,on_delete = models.CASCADE)
    class Meta:
        verbose_name='hospedaje'
        verbose_name_plural='hospedajes'
        ordering= ['nombre_hospedaje']
    def __str__(self):
      return self.nombre_hospedaje
