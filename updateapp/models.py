from django.db import models
class update(models.Model):
    student=models.CharField(max_length=150)
    sno=models.AutoField (primary_key=True)
    classroom=models.IntegerField()
    def __str__(self): 
        return self.student
    class Meta:
        db_table="helo"  
        managed=True
# Create your models here.
