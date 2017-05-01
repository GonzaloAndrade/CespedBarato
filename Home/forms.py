from django import forms
__author__ = 'Gonzalo'


class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    a = forms.CharField(max_length=20)
    #All my attributes here