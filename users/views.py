from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

#Modulo para el tiempo
from datetime import datetime

#Importando recursos de Tweet
from tweet.models import Twitt
from tweet.forms import TwittForm
from tweet.views import Tview

# Create your views here.

class index(ListView):
    model = Twitt
    template_name = 'index.html'


class profile(CreateView):
    model = Twitt
    template_name = 'user/profile.html'
    form_class = TwittForm
    success_url = reverse_lazy('user:profile')

    #Sobreescribiendo el metodo get para mostrar twitts del usuario
    def get_context_data(self, **kwargs):
        context = super(profile, self).get_context_data(**kwargs)

        if 'twitts' not in context:
            context['twitts'] = Tview(User.objects.get(id=User.objects.filter(username=self.request.user)))
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
            #User.objects.get(id=User.objects.filter(username=self.request.user)).id
        return context


    #Sobreescribiendo el metodo post para guardar el twitt correctamente
    def post(self, request, *args, **kwargs):
        #Accediendo al objeto
        self.object = self.get_object
        #Realizando queryset para encontrar el ID del usuario
        user_id = User.objects.get(id=User.objects.filter(username=self.request.user))

        #Extrayendo informacion del formulario (Solamente el campo text)
        form = self.form_class(request.POST)

        #Verificando si la informacion del formulario es valida
        if form.is_valid():
            #Asignando informacion a variable valor
            valor = form.save(commit=False)
            #Asignando llave foranea igualando a el queryset del usuario
            valor.user_twit = user_id
            valor.date_twit = datetime.now()
            #Guardando la informacion en la base de datos
            valor.save()
            #Redireccionando informacion
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, error='1'))
