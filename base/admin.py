from __future__ import unicode_literals

from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin
from easy_select2 import select2_modelform




# Register your models here.



class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ("title", "author", "date_published", "number_of_page", "type_of_book")
	search_fields = ('title', "author")
	class Meta:
		model = 'Book'

admin.site.register(Book, BookAdmin)