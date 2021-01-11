from django.db import models

# Create your models here.
class Playthrough(models.Model):
    characweapon = models.ForeignKey('characters.UsedWeapon',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    weapon = models.IntegerField()
    armor = models.IntegerField()
    head = models.IntegerField()
    arm = models.IntegerField()
    leg = models.IntegerField()
    accessory = models.IntegerField()

class Route(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    area = models.ForeignKey('gamedata.Area',on_delete=models.CASCADE)

class Treeitem(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)

class Meteoritem(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)

class Mithrilitem(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)

class Blooditem(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)

class Moonstoneitem(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)

class Forcecoreitem(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)

class Skilltree(models.Model):
    play_through = models.ForeignKey(Playthrough,on_delete=models.CASCADE)
    skill = models.ForeignKey('characters.Skill',on_delete=models.CASCADE)
    level = models.IntegerField()