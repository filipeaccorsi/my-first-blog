from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): 
# class: definição de um objeto; post: o nome do modelo; models.Model: o post é um modelo de Django
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey: link para um outro modelo
    title = models.CharField(max_length=200)
    # models.CharField: texto com um número limitado de caracteres
    text = models.TextField()
    # models.TextField: campo para textos sem um limite fixo
    created_date = models.DateTimeField(default=timezone.now)
    # models.DateTimeField: data e hora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title