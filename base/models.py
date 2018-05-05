# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Book(models.Model):
	title = models.CharField(max_length=300)
	author = models.CharField(max_length=300)
	date_published = models.DateField(blank=True, null=True)
	number_of_page =  models.IntegerField( blank=True, null=True)
	TYPE = (
		('novel','Novel'),
		('documentation','Documentation'),
		('other','Other')
	)
	type_of_book = models.CharField(max_length=300, choices=TYPE, blank=True, null=True)

	def __unicode__(self):
		return self.title

