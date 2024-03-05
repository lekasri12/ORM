from django.db import models
from django.contrib import admin
class librarybooks_DB(models.Model):
      bookno=models.IntegerField(primary_key="bookno");
      name=models.CharField(max_length=50);
      author=models.CharField(max_length=30);
      genre=models.CharField(max_length=20);
      edition=models.CharField(max_length=5);
class librarybooks_DBAdmin(admin.ModelAdmin):
      list_display=("bookno","name","author","genre","edition");


