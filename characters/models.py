from django.db import models


GENDER = (
    ('', '性別を選んでください'),
    ('unknown', 'unknown'),
    ('man', 'man'),
    ('woman', 'woman'),
)

class Characters(models.Model):
    name = models.CharField('名前', max_length=20)
    gender = models.CharField('性別',max_length=7, choices=GENDER)
    discription = models.CharField('特徴', max_length=1000)
    image = models.ImageField('写真', upload_to='media/', null=True)



