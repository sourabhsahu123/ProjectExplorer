from django.contrib import admin
from .models import Project,Category,Post

# Register your models here.
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Category)