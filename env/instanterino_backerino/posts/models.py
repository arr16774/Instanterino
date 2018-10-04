# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.





class Post (models.Model):
  title = models.CharField(max_length = 100)
  usuario = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
  postContent = models.CharField(max_length = 500)
  likes = models.ManyToManyField(User, 'Like')

class Like (models.Model):
  idUsuario = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
  post = models.ForeignKey(Post,null = True, on_delete = models.SET_NULL)
  date = models.DateTimeField(auto_now_add=True)