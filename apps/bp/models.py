from django.db import models

# Create your models here.
categories = (
  ('morning', 'morning'),
  ('afternoon', 'afternoon'),
  ('evening', 'evening'),
)

class BP(models.Model):

  systolic = models.IntegerField('Systolic', default = 0, blank = False, null = False)
  diastolic = models.IntegerField('Diastolic', default = 0,)
  timing = models.CharField('Time', max_length=20, choices=categories)
  created_at = models.DateField('Noted At', auto_now_add=True)
  updated_at = models.DateField('Update At', auto_now=True)  