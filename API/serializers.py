from rest_framework import serializers
from .models import Question, TestSlot, UserResponse, UserTestAttempt

class QuestionSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = '__all__'


class TestSlotSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = TestSlot
        fields = '__all__'

class UserTestAttemptSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserTestAttempt
        fields = '__all__'