from django.db import models

GENDER = (
    ('', '性別を選んでください'),
    ('unknown', '不明'),
    ('man', '男'),
    ('woman', '女'),
)

class Characters(models.Model):
    name = models.CharField('名前', max_length=20)
    gender = models.CharField(max_length=7, choices=GENDER)
    discription = models.CharField('説明', max_length=1000)