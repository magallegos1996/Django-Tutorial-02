#Esto se hace para añadir nuevos campos a nuestra form, en que un principio solo
#tiene username y password. Lo que se hará es crear una clase que herede de form
#de Django par añadir nuevos campos

from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #Esta clase nos brinda una serie de configuraciones para la form. Una de ellas, por ejemplo
    #es el model al que está anclado (así, cuando se ejecute form.save(), la info será
    # guardada en el model User), los campos que mostrará la form, etc. 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
