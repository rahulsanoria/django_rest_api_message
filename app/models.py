# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class detailmodel(models.Model):

    event = models.CharField(max_length=30)
    token = models.CharField(max_length =30)
    uid = models.IntegerField()
    contact_uid = models.IntegerField()
    contact_name = models.CharField(max_length =30)
    contact_type = models.CharField(max_length =30)
    message_dtm = models.DateField()
    message_uid = models.IntegerField()
    message_cuid = models.IntegerField()
    message_dir = models.CharField(max_length=30)
    message_type = models.CharField(max_length=30)
    message_body = models.TextField(max_length=30)
    ack = models.CharField(max_length=30)