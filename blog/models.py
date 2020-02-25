from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=16)
	author = models.CharField(max_length=16)
	content  = models.TextField()
	posted = models.DateTimeField()

	def __str__(self):
		return f"{self.title} by {self.author}"


class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	commenter = models.CharField(max_length=16)
	email = models.EmailField()
	content  = models.TextField()
	posted = models.DateTimeField()
	
	def __str__(self):
		return f"comment on {self.blog.title} by {self.commenter}"
