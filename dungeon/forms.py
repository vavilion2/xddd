from django.contrib.auth import get_user
from django import forms
from django.contrib.auth import get_user_model
from .models import Zayavka
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UsernameField



User=get_user_model()


class ZayavkaForma(forms.ModelForm):

  #  def __init__(self, *args, **kwargs):
  #      super().__init__(*args, **kwargs)
  #      self.fields['user'].queryset = Zayavka.objects.filter()
    class Meta:
        model=Zayavka

        fields='__all__'

class ZayavkaForma1(forms.ModelForm):

    '''
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = Zayavka.objects.filter(user__is_rabotyaga=True)
    '''
    class Meta:
        model = Zayavka


        fields=(
            'user',
        )


class ZayavkaForma2(forms.ModelForm):
   # Zayavka.objects.filter()

    class Meta:
        model=Zayavka


        fields=(
            'imya',
            'familiya','tip','text',
            #'cleent',
        )



      #  def __init__(self, *args, **kwargs):
      #      super().__init__(*args, **kwargs)
      #      self.fields['cleent'].queryset = Zayavka.objects.filter(user=self.initial['user'])



class ZayavkaForma3(forms.ModelForm):
    Zayavka.objects.filter()

    class Meta:
        model = Zayavka

        fields=(
            'cleent',
        )

class ZayavkaForma4(forms.ModelForm):
    Zayavka.objects.filter()

    class Meta:
        model = Zayavka

        fields=(
            'status',
        )



class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=('username',)
        field_classes={'username':UsernameField}