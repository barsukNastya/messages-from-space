# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class MessageFromSpace(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    is_read = models.BooleanField(default=False)




    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    #
    # def __str__(self):
    #     return self.title