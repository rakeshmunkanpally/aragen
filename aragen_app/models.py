from django.db import models



class operation_lookup(models.Model):
    code=models.CharField(max_length=50)
    label=models.CharField(max_length=50)
    revision=models.CharField(max_length=50)
    
    def __str__(self):
        return self.code



    


