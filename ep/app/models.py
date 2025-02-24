from django.db import models

# Create your models here.
CATAGORY= (
     ('MO','Mens Outfit'),
    ('WO','Womens Outfit'),
    ('KO','Kids Outfit')
    
    )

# superuserpass=@J1234

class Product(models.Model):
    title= models.CharField(max_length=100)
    price= models.IntegerField()
    description= models.TextField()
    catagory=models.CharField(choices=CATAGORY,max_length=100)
    image= models.ImageField(upload_to='product')
    def __str__(self):
        return (self.title)


