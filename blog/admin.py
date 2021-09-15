from django.contrib import admin
from .models import Post

#Adicionando post na pagina de admin
admin.site.register(Post)
