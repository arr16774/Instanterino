from django.core.management.base import BaseCommand
from posts.models import Post 
from posts.models import Like
from django.contrib.auth.models import User

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    menuPrincipal = True
    menuPersonal = False
    while(True):
      while(menuPrincipal):
        print("Bienvenido al menu")
        print("1. Crear Usuario")
        print("2. Listar Usuario")
        print("3. Acceder")
        print("4. Salir")
        opcion = input("Opcion Seleccionada: ")

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
          try:
            login = User.objects.get(username = usuario,  email = email)
            menuPersonal = True
            menuPrincipal = False
            print("bienvenido: " + login.username)
          except:
            ("Oops! nose encontro el usuario")
        
        elif(opcion == 4):
          print("hasta luego")
          break

      while(menuPersonal):
        print("1. Crear Post")
        print("2. Like Usuario")
        print("3. Delete Post")
        print("4. Salir")
        opcionPersonal = input("Ingrese la opcion deseada: ")

        if(opcionPersonal == 1):
          print("Cree su Post")
          tituloDePost = raw_input("Ingrese su Titulo: ")
          contenidoPost = raw_input("Ingrese su Contenido: ")
          post = Post(title = tituloDePost, usuario = login, postContent = contenidoPost)
          post.save()
        if(opcionPersonal == 2):
          for post in Post.objects.all():
            print("post = {}: {} {}".format(post.pk,post.title,post.usuario))
          post_likeao_id = input("Ingrese el id del post que desea darle un like: ")
          post_likeao = Post.objects.get(id = post_likeao_id)
          likerino = Like(usuario_id = login, posterino = post_likeao)
          likerino.save()
        if(opcionPersonal == 3):
          for post in Post.objects.all():
            print("post = {}: {} {}".format(post.pk,post.title,post.usuario))
          post_deleteado_id = input("Ingrese el id del post que desea borrar: ")
          post_deleteado = Post.objects.get(id = post_deleteado_id)
          post_deleteado.delete()
          








      
      




    

