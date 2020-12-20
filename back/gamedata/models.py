from django.db import models

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{0} {1}'.format(self.name,self.pk)

class Animal(models.Model):
    name = models.CharField(max_length=255)
    first_appear = models.IntegerField(default=60)
    skill = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    kinds = models.IntegerField()
    rank = models.IntegerField()
    max_quantity = models.IntegerField(default=1)
    stats = models.TextField()
    material_left = models.IntegerField()
    material_right = models.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.name, self.pk)


class AreaItem(models.Model):
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)
    area_id = models.ForeignKey(Area,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '{0} {1}'.format(self.area_id.name,self.item_id.name)

class AreaAnimal(models.Model):
    area_id = models.ForeignKey(Area,on_delete=models.CASCADE)
    animal_id = models.ForeignKey(Animal,on_delete=models.CASCADE)
    respon_amount = models.IntegerField(default=1)
    
    def __str__(self):
        return '{0} {1}'.format(self.area_id.name,self.animal_id.name)

class AnimalItem(models.Model):
    animal_id = models.ForeignKey(Animal,on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE)
    get_percent = models.FloatField(default=0)
    pocket_number = models.IntegerField(default=1)

    def __str__(self):
        return '{0} {1} {2}'.format(self.animal_id.name,self.item_id.name,self.pocket_number)