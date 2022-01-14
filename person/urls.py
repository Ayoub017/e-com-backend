from django.urls import path 
from . import views 
from django.urls import path 
from . import views 

urlpatterns = [
    path('persons/',views.getpersons),
    path('person/<str:username>/',views.getPersonByUsername),
    path('addperson/',views.addPersons),
    path('updateperson/<int:id>/',views.updatePerson),
    path('deleteperson/<int:id>/',views.deletePerson),
    path('authenticate/',views.authentication),
    path('products/',views.getProducts),
    path('addproduct/',views.addProduct),
    path('commandes/',views.getCommandes),
    path('commandes/<int:id>/',views.getCommandesByIdClient),
    path('updatestatus/',views.updateCommandeStatus)
]