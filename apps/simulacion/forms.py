from django import forms
from django.core.exceptions import ValidationError
from .models import DatoEntrada,  VariableMacro 



class EntradaForm(forms.ModelForm):
	class Meta:
		model =DatoEntrada

		fields=[
			'salario',
			'renta',
			'ganancias',
			'interes',
			'impuestos_indirectos',
			'depreciacion',
			'subsidios',
			'poblacion',
			'can_Ampliada',
			'salario_Minimo',
			'anios_simulados',
			'iva_simulado',
		]

		labels={
			'salario': 'Salario',
			'renta':'Renta',
			'ganancias': 'Ganancias',
			'interes': 'Intereses',
			'impuestos_indirectos':'Impusos Indirectos',
			'depreciacion': 'Depreciacion',
			'subsidios':'Subsidios',
			'poblacion':'Poblacion',
			'can_Ampliada': 'Canasta Ampliada',
			'salario_Minimo': 'Salario Minimo',
			'anios_simulados':'Anios a simular',
			'iva_simulado': 'Iva a Simular en %',
		}


		widgets={
			'salario': forms.NumberInput(attrs={'class':'form-control'}),
			'renta':forms.NumberInput(attrs={'class':'form-control'}),
			'ganancias':forms.NumberInput(attrs={'class':'form-control'}),
			'interes':forms.NumberInput(attrs={'class':'form-control'}),
			'impuestos_indirectos':forms.NumberInput(attrs={'class':'form-control'}),
			'depreciacion':forms.NumberInput(attrs={'class':'form-control'}),
			'subsidios':forms.NumberInput(attrs={'class':'form-control'}),
			'poblacion':forms.NumberInput(attrs={'class':'form-control'}),
			'can_Ampliada':forms.NumberInput(attrs={'class':'form-control'}),
			'salario_Minimo':forms.NumberInput(attrs={'class':'form-control'}),
			'anios_simulados':forms.NumberInput(attrs={'class':'form-control'}),
			'iva_simulado':forms.NumberInput(attrs={'class':'form-control'}),
		}












