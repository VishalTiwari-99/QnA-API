from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    ANS_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, default = date.today(), null=True)
    question_english = models.TextField(null=True)
    option_one_english = models.TextField(null=True)
    option_two_english = models.TextField(null=True)
    option_three_english = models.TextField(null=True)
    option_four_english = models.TextField(null=True)

    question_hindi = models.TextField(null=True)
    option_one_hindi = models.TextField(null=True)
    option_two_hindi = models.TextField(null=True)
    option_three_hindi = models.TextField(null=True)
    option_four_hindi = models.TextField(null=True)

    answer = models.CharField(max_length=10, choices = ANS_CHOICES, null=True)
    fresh = models.BooleanField(default=True)
    created = models.DateField(auto_now = False, auto_now_add = True, editable=False)
    updated = models.DateField(auto_now = True, auto_now_add = False, editable=False)

    @property
    def get_answer(self):
        if(self.answer=='1'):
            ans = [self.option_one_english, self.option_one_hindi]
        elif(self.answer=='2'):
            ans = [self.option_two_english, self.option_two_hindi]
        elif(self.answer=='3'):
            ans = [self.option_three_english, self.option_three_hindi]
        else:
            ans = [self.option_four_english, self.option_four_hindi]
        return ans
    
    def __str__(self):
        return str(self.date)+"_"+self.question_english[:10]+"...."+self.question_english[-10:]



class TestSlot(models.Model):
    Time = (
        ('Morning', 'M'),
        ('Evening', 'E'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    question_list = models.ManyToManyField(Question)
    time_slot = models.CharField(max_length=10, choices=Time, null=True)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now = False, auto_now_add = True, editable=False)
    updated = models.DateField(auto_now = True, auto_now_add = False, editable=False)


