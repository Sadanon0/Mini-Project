from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    # การปรับแต่งการแสดงผลของฟิลด์แต่ละฟิลด์
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control border rounded-md shadow-sm bg-white px-4 py-2',
            'placeholder': 'ระบุชื่อสินค้า',
            'required': 'required',
        }),
        label='ชื่อสินค้า'
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control border rounded-md shadow-sm bg-white px-4 py-2',
            'placeholder': 'ระบุที่อยู่ของคุณ',
            'rows': 4,
            'required': 'required',
        }),
        label='ที่อยู่ของคุณ'
    )
    
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control border rounded-md shadow-sm bg-white px-4 py-2',  # ผสม bootstrap และ tailwind
            'placeholder': 'ระบุจำนวน',
            'min': '0',
            'step': '1',
            'required': 'required',
        }),
        label='จำนวน'
    )

class CustomUserCreationForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')