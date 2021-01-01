from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255)
    attack = models.FloatField()
    attack_growth = models.FloatField()
    shield = models.FloatField()
    shield_growth = models.FloatField()
    health = models.IntegerField()
    health_growth = models.IntegerField()
    health_regen = models.FloatField()
    health_regen_growth = models.FloatField()
    stamina = models.IntegerField()
    stamina_growth = models.IntegerField()
    stamina_regen = models.FloatField()
    stamina_regen_growth = models.FloatField()
    attack_speed = models.FloatField()
    attack_speed_growth = models.FloatField(default=0)
    critical = models.FloatField(default=0)
    critical_growth = models.FloatField(default=0)
    moving_speed = models.FloatField()
    moving_speed_growth = models.FloatField(default=0)
    eyesight = models.IntegerField(default=8)
    eyesight_growth = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ampli(models.Model):
    charac = models.ForeignKey(Character,on_delete=models.CASCADE)
    mode = models.CharField(max_length=100)
    damage_taken = models.FloatField(default=0)
    damage_done = models.FloatField(default=0)

    def __str__(self):
        return '{0} {1}'.format(self.charac.name,self.mode)

class Skill(models.Model):
    charac = models.ForeignKey(Character,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    button = models.CharField(max_length=255)
    stats = models.TextField()
    detail = models.TextField()
    is_basic = models.CharField(max_length=255,default='basic')

    def __str__(self):
        return '{0} {1}'.format(self.charac.name,self.name)

class Weapon(models.Model):
    name = models.CharField(max_length=255)
    attack_speed = models.FloatField()
    attack_speed_growth = models.FloatField()
    additional_damage = models.FloatField()
    additional_damage_growth = models.FloatField()
    amplify_skill_damage = models.FloatField()
    amplify_skill_damage_growth = models.FloatField()
    skill_stats = models.TextField(default='')
    skill_detail = models.TextField(default='')

    def __str__(self):
        return self.name

class UsedWeapon(models.Model):
    charac = models.ForeignKey(Character,on_delete=models.CASCADE)
    weapon_name = models.ForeignKey(Weapon,models.CASCADE)

    def __str__(self):
        return '{0} {1} {2}'.format(self.charac.name,self.weapon_name.name,self.pk)

class RealAmpli(models.Model):
    charac = models.ForeignKey(Character,on_delete=models.CASCADE)
    weap = models.ForeignKey(Weapon,on_delete=models.CASCADE)
    mode = models.CharField(max_length=100)
    damage_taken = models.FloatField(default=0)
    damage_done = models.FloatField(default=0)

    def __str__(self):
        return '{0} {1} {2}'.format(self.charac.name,self.mode,self.weap.name)

class ModeWeaponCharacterAmpli(models.Model):
    charac_weapon = models.ForeignKey(UsedWeapon,on_delete=models.CASCADE)
    SoloDamageTaken = models.FloatField()
    SoloDamageGive = models.FloatField()
    DuoDamageTaken = models.FloatField()
    DuoDamageGive = models.FloatField()
    SquadDamageTaken = models.FloatField()
    SquadDamageGive = models.FloatField()

    def __str__(self):
        return '{0} {1} 증폭'.format(self.charac_weapon.charac.name, self.charac_weapon.weapon_name.name)

class WeaponCharacterStat(models.Model):
    charac_weapon = models.ForeignKey(UsedWeapon,on_delete=models.CASCADE)
    mode = models.CharField(max_length=100)
    is_ranker = models.BooleanField()
    win_rate = models.FloatField()
    pick_rate = models.FloatField()
    avg_kill = models.FloatField()
    avg_rank = models.FloatField()
    
    def __str__(self):
        if self.is_ranker:
            text = '랭커'
        else:
            text = '전체'
        return '{0} {1} {2} {3} 통계'.format(self.charac_weapon.charac.name,self.charac_weapon.weapon_name.name,text,self.mode)

class WeaponStat(models.Model):
    charac_weapon = models.ForeignKey(UsedWeapon,on_delete=models.CASCADE)
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)
    mode = models.CharField(max_length=100)
    win_rate = models.FloatField()
    pick_rate = models.FloatField()

    def __str__(self):
        return '{0} {1} {2} {3} 통계'.format(self.charac_weapon.charac.name,self.charac_weapon.weapon_name.name,self.item.name,self.mode)

class ArmorStat(models.Model):
    item = models.ForeignKey('gamedata.Item',on_delete=models.CASCADE)
    mode = models.CharField(max_length=100,default='')
    win_rate = models.FloatField(default=0)
    solo_win = models.FloatField(default=0)
    duo_win = models.FloatField(default=0)
    squad_win = models.FloatField(default=0)

    def __str__(self):
        return '{0} 승률 통계'.format(self.item.name)