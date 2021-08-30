from django.contrib import admin
from .models import Question, MakeTest, UserResponse, UserTestAttempt

# Register your models here.
admin.site.register(Question)
admin.site.register(MakeTest)
admin.site.register(UserResponse)
admin.site.register(UserTestAttempt)