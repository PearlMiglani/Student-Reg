from django.db import models

# Create your models here.
class emp(models.Model):
    #try:
    
        
    
    num=0
        
    empAge= models.IntegerField()
    empname= models.CharField(max_length=100)
    empadress=models.CharField(max_length=100)
    stream=models.CharField(max_length=6)
    Category=models.CharField(max_length=6)
    date= models.DateField()
    year= models.IntegerField()
    salary= models.DecimalField(max_digits=5, decimal_places=2)
    img = models.FileField(default="contacts-icon-256-200x200.jpg",upload_to="photos")
    primary_id= models.CharField(max_length=50, primary_key=True)
    
    
    #def __init__(self):
    #    models.Model.__init__(self)
    #    emp.num+=1

    def getnum():
        #num = cls(num=num+=1)
        emp.num+=1
        return str(emp.num)
    
    

    
