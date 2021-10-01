from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from .managers import ZayavkaManager
from django.db.models.signals import post_save






class User(AbstractUser):
    is_rabotyaga = models.BooleanField(default=False, null=True, blank=True)
    is_manadger = models.BooleanField(default=False, null=True, blank=True)
    is_client = models.BooleanField(default=True, null=True, blank=True)
    pass






class TipRabot(models.Model):
    tip_rabot=models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.tip_rabot






class Zayavka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    data=models.DateTimeField(auto_now_add=True)
    imya = models.CharField(max_length=150, blank=False)
    familiya = models.CharField(max_length=150,blank=False)

    tip = models.ForeignKey(TipRabot, on_delete=models.CASCADE)
    text=models.TextField(max_length=500,blank=True)
    status=models.BooleanField(default=False)
    cleent=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='cleent')

 #   trudyashiysya=models.ForeignKey(RabotyagaProx,on_delete=models.CASCADE,null=True,blank=True)

    objects=ZayavkaManager()

    class Meta:
        ordering = ['user','status',"-data"]

    def __str__(self):
        return self.imya

'''
class ClientProfile(models.Model):
    client=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    xd=models.OneToOneField(Zayavka,on_delete=models.CASCADE,null=True,blank=True)
    pass


def createl(sender, instance, created, **kwargs):
    if created:
        Zayavka.objects.create(client=instance)

post_save.connect(createl,sender=User)
'''





'''
class ManadgerProx(models.Model):
    manadger = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    is_manadger = models.BooleanField(default=False,null=True,blank=True)


class ClientProx(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    is_client = models.BooleanField(default=True,null=True,blank=True)


class RabotyagaProx(models.Model):
    rabotyaga = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    is_rabotyaga = models.BooleanField(default=False,null=True,blank=True)

'''






