# -*-coding:utf-8-*-
from django.forms import ModelForm, TextInput, Form
from django import forms
from .models import Product, Brand, Client, Favorite, Review
from django.db import models

class RegisterProduct(forms.Form):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {'title': TextInput(
            attrs={'class': 'form-control'})}


class RegisterBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {'name': TextInput(
            attrs={'class': 'form-control'})}


class RegisterFavorite(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = '__all__'
       
class RegisterReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
       

class RegisterClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {'name': TextInput(
            attrs={'class': 'form-control'})}