from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #Esta funcion se utiliza para que, cuando se cree un nuevo post, automáticamente nos redirija a la pagina de
    #de detalles del nuevo post. En caso de que querramos que nos redirija a HOME, deberías en cambio especificar 
    #un atributo en la clase 'PostCreateView' llamado 'successUrl' con el valor del nombre de la url para home; es decir
    #con 'blog-home'
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

