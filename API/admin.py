from django.contrib import admin
from .models import Question, TestSlot, UserResponse, UserTestAttempt

# Register your models here.
admin.site.register(Question)
admin.site.register(TestSlot)
admin.site.register(UserResponse)
admin.site.register(UserTestAttempt)