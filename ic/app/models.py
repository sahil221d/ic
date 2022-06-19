from django.db import models

# Create your models here.


class Fort(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    fort_image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)

class Food(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    food_image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = ( 
   ('M', 'Museum Paintings'),
   ('P', 'Painting Fortfolio'),
)

class painting(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)


class PerfArts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pa_image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = ( 
   ('R', 'Rare Books'),
   ('I', 'Images'),
   ('N', 'Newspaper Clippings'),
)

class freedomar(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4)
    fr_image = models.ImageField(upload_to='producting')

  

    def __str__(self):
        return str(self.id)



CATEGORY_CHOICES = ( 
   ('A', ' Avanaddha Vadya'),
   ('T', 'Tat Vadya'),
   ('G', 'Ghan Vadya'),
   ('S', 'Sushir Vadya'),
)

class musicali(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4)
    instru_image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = ( 
   ('W', ' Weaving'),
   ('P', ' Printing'),
   ('E', 'Embroidery'),
)

class textile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)