from __future__ import unicode_literals

from django.db import models
from djangotoolbox.fields import ListField

Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=200, null=False)
	desc = models.CharField()
	created_by = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
	tag = models.CharField(max_length=50, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class TaskTags(models.Model):
	task_id = models.ForeignKey(Task)
	tag_id = models.ForeignKey(Tag)


# # Create your models here.
# class Task(models.Model):
# 	title = models.CharField(max_length=200)
# 	desc = models.CharField()
# 	tags = ListField()
# 	created_by = models.CharField(max_length=50)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now_add=True)

