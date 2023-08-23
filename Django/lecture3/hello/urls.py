from django.urls import path
from . import views #Del actual directorio importamos el archivo views

urlpatterns = [
    path("", views.index, name="index") #Cuando visitemos la página del primer argumento, lo que queremos renderizar es view.index del segundo argumento, y le damos un nombre a esa URL
]