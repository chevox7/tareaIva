from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class DatoEntrada(models.Model):
	salario= models.DecimalField(decimal_places=2, max_digits=10)
	renta= models.DecimalField(decimal_places=2, max_digits=10)
	ganancias= models.DecimalField(decimal_places=2, max_digits=10)
	interes= models.DecimalField(decimal_places=2, max_digits=10)
	impuestos_indirectos= models.DecimalField(decimal_places= 2, max_digits= 10)
	depreciacion= models.DecimalField(decimal_places= 2, max_digits= 10)
	subsidios= models.DecimalField(decimal_places=2, max_digits=10)
	poblacion= models.IntegerField()
	can_Ampliada= models.DecimalField( decimal_places=2, max_digits=10)
	salario_Minimo=models.DecimalField( decimal_places=2, max_digits=10)
	anios_simulados=models.IntegerField()	
	iva_simulado = models.DecimalField( decimal_places=2, max_digits=10)



class VariableMacro(models.Model):
	codigo=models.CharField(max_length=10,primary_key=True)
	nombreMacro= models.CharField(max_length= 50)
	abreviatura= models.CharField(max_length= 50)
	tipo= models.CharField(max_length= 50)
	valor= models.DecimalField(max_digits=19, decimal_places=4)
	
	def __str__(self):
	 return self.abreviatura


class Simulacion(models.Model):
	nombreSim= models.CharField(max_length= 50)
	fecha=  models.DateField(auto_now_add=timezone.now().date())
	usuario= models.ForeignKey(User, null= True, blank= True, on_delete= models.CASCADE)
	varEntrada = models.OneToOneField(DatoEntrada,null= True, blank= True, on_delete= models.CASCADE)
	variablesM=models.ManyToManyField(VariableMacro, blank=True)

	def __str__(self):
	 return self.nombreSim	 