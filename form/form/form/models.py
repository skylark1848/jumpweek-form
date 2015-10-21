from django.db import models
from forms import NameForm

class Person(models.Model):
    your_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.your_name