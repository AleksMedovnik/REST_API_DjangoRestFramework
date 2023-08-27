from django.db import models


class Color(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'color'


class Maker(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'maker'


class OS(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'os'
        verbose_name_plural = 'OS'


class RAM(models.Model):
    value = models.FloatField()

    def __str__(self) -> str:
        return f'{str(self.value)} ГБ' 

    class Meta:
        db_table = 'ram'
        verbose_name_plural = 'ram'