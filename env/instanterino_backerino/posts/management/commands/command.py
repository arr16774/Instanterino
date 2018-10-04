from django.core.management.base import BaseCommand
from posts.models import Post 
from django.contrib.auth.models import User

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    while(True):
      print("Bienvenido al menu")
      print("1. Crear Usuario")
      print("2. Listar Usuario")
      print("3. Acceder")
      print("4. Salir")
      opcion = input("Opcion Seleccionada")

      if(opcion == 1):
        print("Cree un Usuario")
        nombre = raw_input("Ingrese su nombre: ")
        apellido = raw_input("Ingrese su apellido: ")
        email = raw_input("Ingrese su email: ")
        username = raw_input("Ingrese su usuario: ")
        mi_usuario = User(first_name = nombre, last_name = apellido, email = email, username = username)
        mi_usuario.save()
        print(User.objects.all())

      elif(opcion == 2):
        for user in User.objects.all():
          print("pk = {}: {} {} - {}".format(user.pk,user.first_name,user.last_name,user.email,user.username))
      
      elif(opcion == 3):
        usuario = raw_input("Ingrese su usuario: ")
        email = raw_input("Ingrese su email: ")
        login = User.objects.get(username = usuario,  email = email)
        print("bienvenido: " + login.username)
      
      elif(opcion == 4):
        print("hasta luego")
        break






      
      




    

