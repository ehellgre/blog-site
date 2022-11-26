from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post) # Now the database shows on our admin panel (the one that we created on models.py file)