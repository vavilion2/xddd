from django.shortcuts import render,reverse,redirect,HttpResponseRedirect,get_object_or_404
from django.views import generic
from .models import Zayavka#,RabotyagaProx
from .forms import ZayavkaForma,ZayavkaForma1,ZayavkaForma2,ZayavkaForma3,ZayavkaForma4
from django.views.decorators.csrf import csrf_protect
from .perm import ManDostup,CliDostup,RabDostup,LoginRequiredMixin,AccessMixin
from django.utils.decorators import method_decorator

class LandingView(generic.TemplateView):
    template_name='shlak/landing.html'


class ZayavkaDetali( ManDostup, generic.DetailView):
    template_name = 'dungeon/zayavka_detali.html'
    context_object_name = 'zayavka'

    def get_queryset(self):
        queryset=Zayavka.objects.filter()
        return queryset

class ZayavkaSpisok(ManDostup, generic.ListView):
    template_name = 'dungeon/zayavka_spisok.html'
    context_object_name = 'zayavka'

    def get_queryset(self):
        queryset= Zayavka.objects.filter()
        return queryset



class ZayavkaUpdate(ManDostup, generic.UpdateView):
    template_name = 'dungeon/zayavka_update.html'
    form_class = ZayavkaForma1

    def get_queryset(self):
        query=Zayavka.objects.filter()
        return query


    def get_success_url(self):
        return reverse ('zayavki:zayavka-spisok')


class ZayavkaCreate(CliDostup, generic.CreateView):
    template_name ='dungeon/zayavka_create.html'
    form_class = ZayavkaForma1


    def get_queryset(self):
        query=Zayavka.objects.exclude()
        return query

    def get_success_url(self):
        return reverse('zayavki:zayavka-spisok')

class ZayavkaDelete(ManDostup, generic.DeleteView):
    template_name ='dungeon/zayavka_delete.html'
    form_class = ZayavkaForma1

    def get_queryset(self):
        query = Zayavka.objects.exclude()
        return query

    def get_success_url(self):
        return reverse ('zayavki:zayavka-spisok')



class ZayavkaSpisokR(RabDostup,generic.ListView):
    template_name = ('rabotyaga_interf/zayavka_spisok_r.html')
    context_object_name = 'zayavka'

    def get_queryset(self):
        query=Zayavka.objects.filter(user__username=self.request.user,status=False)

        return query



class ZayavkaSpisokC(CliDostup, generic.ListView):
    template_name = ('client_interf/zayavka_spisok_c.html')
    context_object_name = 'zayavka'

    def get_queryset(self):
        query=Zayavka.objects.filter(cleent__username=self.request.user)
        return query
'''
class ZayavkaCreateC(generic.CreateView):
    template_name = ('client_interf/zayavka_create_c.html')
    form_class = ZayavkaForma2


    def get_success_url(self):
        return reverse ('zayavki:zayavka-spisok-c')
'''


#def dispatch(self, request, *args, **kwargs):
#    if not request.user.is_authenticated or not request.user.is_manadger:
#        return redirect('landing-p')
#    return super().dispatch(request, *args, **kwargs)
#
@csrf_protect
def zayavka_create_c_def(request):
    if not request.user.is_authenticated or not request.user.is_client:
        return redirect('landing-p')
    form =ZayavkaForma2

    if request.method == "POST":
        form = ZayavkaForma2(request.POST, request.FILES)
        if form.is_valid():
            xd = form.save(commit=False)
            xd.cleent = request.user
            xd.save()
            return HttpResponseRedirect(reverse('zayavki:zayavka-spisok-c'))
    return render(request, 'client_interf/zayavka_create_c.html', {
        'form': form
    })





class ZayavkaDetaliC(CliDostup,generic.DetailView):
    template_name = ('client_interf/zayavka_detali_c.html')
    queryset = Zayavka.objects.filter()


class ZayavkaUpdateR(RabDostup, generic.UpdateView):

    template_name = ('rabotyaga_interf/zayavka_obnovit.html')
    form_class = ZayavkaForma4
    queryset = Zayavka.objects.filter()

    def get_success_url(self):
        return reverse ('zayavki:zayavka-spisok-r')
