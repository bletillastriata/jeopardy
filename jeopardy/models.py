from django.db import models

# Create your models here.

class Clue(models.Model):
	# index = models.IntegerField()
	# clue_id = models.OneToOneField(clue_id, primary_key=True)
	clue_id = models.FloatField()
	answer = models.CharField(max_length=500)
	question = models.CharField(max_length=500)
	value = models.FloatField()
	airdate = models.DateField()
	# created_date = models.CharField(max_length=500)
	# updated_date = models.CharField(max_length=500)
	category = models.TextField()
	cate_id = models.FloatField()
	category_info = models.CharField(max_length=500)

	def __str__(self):
		return "Question %d: %s" %(self.clue_id, self.question)


		

