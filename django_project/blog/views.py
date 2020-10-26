from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Blog'
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    #es necesario establecerlo porque por defecto, la ListView class buscará un template con el siguiente formato
    #<app>/<model>_<viewtype>.html; es decir, buscará 'blog/post_listview.html
    template_name = 'blog/home.html'
    #es necesario establecerlo porque por defecto, la ListView class nombrará a la lista de objetos como 'object_list'
    #pero nosotros la nombramos como 'posts'
    context_object_name = 'posts' 
    #Si hubiéramos seguido los nombres por defecto que usa ListView, no tendríamos que especificar nada más que el
    #modelo que va a usar (Post) y el orden en el que se van a mostrar dichos modelos; mostrando de esa manera, el 
    #beneficio de usar Generic View (en este caso ListView) en lugar de definir una view como una función
    #Para denotar esto, vamos a seguir las convenciones de Generic View para futuras views
    ordering = ['-date_posted'] #-date_posted es para que ordene los post del más reciente al más viejo
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' 
    paginate_by = 5

    #Se realiza un override de la funcion get_queryset para establecer que post se van a listar en la generic view
    #ListView. En este caso, queremos posts que que haya sido creados por un cierto usuario y que se ordenen del más
    #nuevo al mas antiguo
    def get_queryset(self):
        #username=self.kwargs.get('username') me permite obtener los query parameters de la URL
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


#Notar que ahora, para la generic class DetailView, tenemos una view perfectamente funcional con pocas lineas de código
#En este caso, el único atributo que se definió fue el model sobre el que va a trabajar esta generic view
#Esto se debe a que hemos seguido las conveciones de esta generic View nombrando, por ejemplo, a la variable
#que espera esta view de la URL como 'pk' o nombrando el objeto que usa para mostrar los detalles en el template como
#'object' o nombrando el archivo de template siguiendo este formato: <app>/<model>_<viewtype>.html
class PostDetailView(DetailView):
    model = Post

#Notar el primer argumento 'LoginRequiredMixin'. Este es similar al decorator @login_required utilizado en la app
#'users' para para las generic Class y evita que pueda acceder a esta view sin estar loggeado. Si lo intenta, será
#redirigido a la página de Login
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #Se realiza un override de la funcion form_valid de la clase CreateView para especificarle que, antes de realizar
    # el submit de la form, tome la instancia de esta form y setee el author como el usuario loggeado actualmente 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Nota el segundo argumento. Esto permitirá que solo el usuario o autor que haya creado el post sea capaz de 
#actualizarlo. Es decir, que ningún usuario pueda actualizar un post de otro usuario 
#Para ello, se hace un override de la función testFunc, se obtiene el objeto sobre el que esta trabajando la
# generic view UpdateView con 'get_object()' (que en este caso es el objeto post que devuelva el pk de la url 
# 'post-update'), se obtiene el current user que esta loggeado y se comparan si son los mismos. 
# Si son, se devuelve true, sino false
#También notar que para esta View no se creó un nuevo template, puesto que CreateView y UpdateView
#hacen uso del mismo: 'post_form'
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
        
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
