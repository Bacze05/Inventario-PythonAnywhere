from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Submit, Button



class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'producto', 'cantidad', 'precio', 'descuento']

    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get('cantidad')
        precio = cleaned_data.get('precio')

        # Realiza validaciones adicionales según tu lógica de negocio
        if cantidad and cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor que cero.")

        if precio and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")

        return cleaned_data




