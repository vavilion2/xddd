from django.contrib import admin
from .models import User,Zayavka,TipRabot
    #RabotyagaProx,ClientProx,ManadgerProx
    #ClientProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

'''

class MInLIne(admin.StackedInline):
    model = ManadgerProx
    can_delete = False
    verbose_name = 'manadger'

class RInLIne(admin.StackedInline):
    model = RabotyagaProx
    can_delete = False
    verbose_name = 'rabochiy'

class CInLIne(admin.StackedInline):
    model = ClientProx
    can_delete = False
    verbose_name = 'client'


class UserAdmin(BaseUserAdmin):
    inlines = (CInLIne,RInLIne,MInLIne)



'''


admin.site.register(User)
admin.site.register(TipRabot)
admin.site.register(Zayavka)
'''
#admin.site.register(ClientProfile)
admin.site.register(RabotyagaProx)
admin.site.register(ClientProx)
admin.site.register(ManadgerProx)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

'''
