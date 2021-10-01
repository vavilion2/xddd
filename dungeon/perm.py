from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Zayavka
from django.contrib.auth.mixins import AccessMixin,LoginRequiredMixin
from django.shortcuts import redirect




#content_t=ContentType.objects.get_for_model(Zayavka)
#perm=Permission.objects.create(
#    codename=
class ManDostup(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_manadger:
            return redirect('landing-p')
        return super().dispatch(request, *args, **kwargs)

class RabDostup(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_rabotyaga:
            return redirect('landing-p')
        return super().dispatch(request, *args, **kwargs)

class CliDostup(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_client:
            return redirect('landing-p')
        return super().dispatch(request, *args, **kwargs)


