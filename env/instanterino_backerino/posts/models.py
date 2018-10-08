# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Post (models.Model):
  title = models.CharField(max_length = 100)
  usuario = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
  postContent = models.CharField(max_length = 500)
  date = models.DateTimeField(auto_now_add=True)
  

class Like (models.Model):
  usuario_id = models.ForeignKey(User,null=True, on_delete = models.CASCADE)
  posterino = models.ForeignKey(Post,null = True, on_delete = models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)