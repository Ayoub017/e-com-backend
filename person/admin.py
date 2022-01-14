from django.contrib import admin
from person.models import Person,Product,Commande
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



# class CustomUser(admin.StackedInline):
#    model = Person

# class CustomUserPerson(UserAdmin):
#     inLines = (CustomUser,)
  
admin.site.register(Person)
# Register your models here.
admin.site.register(Product)
admin.site.register(Commande)