from django.db import models

# Create your models here.
class User(models.Model):

	gender = (
		('male',"男"),
		('female',"女"),
	)

	name = models.CharField(max_length=50,unique=True)
	password = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	mobile = models.CharField(max_length=22,default="电话")
	sex = models.CharField(max_length=32,choices=gender,default="男")
	department = models.CharField(max_length=30,default="部门") # 部门
	position = models.CharField(max_length=30,default="职位")   # 职位
	Job_number = models.CharField(max_length=30,default="工号") # 工号

	c_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-c_time"]
		verbose_name = "用户"
		verbose_name_plural = "用户"