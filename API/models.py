from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Question(models.Model):
    ANS_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    question_english = models.TextField(null=True)
    question_hindi = models.TextField(null=True)

    option_one = models.TextField(null=True)
    option_two = models.TextField(null=True)
    option_three = models.TextField(null=True)
    option_four = models.TextField(null=True)
    correct_answer = models.CharField(max_length=10, choices = ANS_CHOICES, null=True)
    fresh = models.BooleanField(default=True)
    created = models.DateField(auto_now = False, auto_now_add = True, editable=False)
    updated = models.DateField(auto_now = True, auto_now_add = False, editable=False)

    @property
    def get_answer(self):
        if(self.answer=='1'):
            ans = self.option_one
        elif(self.answer=='2'):
            ans = self.option_two
        elif(self.answer=='3'):
            ans = self.option_three
        else:
            ans = self.option_four
        return ans
    
    def __str__(self):
        return str(self.date)+"_"+self.question_english[:10]+"...."+self.question_english[-10:]



class TestSlot(models.Model):
    Time = (
        ('M', 'Morning'),
        ('E', 'Evening'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    question_list = models.ManyToManyField(Question)
    time_slot = models.CharField(max_length=10, choices=Time, null=True)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now = False, auto_now_add = True, editable=False)
    updated = models.DateField(auto_now = True, auto_now_add = False, editable=False)

class UserResponse(models.Model):
    RESPONSE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    test = models.ForeignKey('UserTestAttempt', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    response = models.CharField(max_length=10, choices=RESPONSE_CHOICES, null=True)


class UserTestAttempt(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    assigned_test = models.ForeignKey('TestSlot', on_delete=models.CASCADE)
    is_attempted = models.BooleanField(default=False)
    score = models.FloatField(null=True)


