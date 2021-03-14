from django.contrib import admin
from .models import Mogwai, Feeding, Toy, Photo

# Register your models here.
admin.site.register(Mogwai)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)
