from rest_framework import serializers
from .models import Question, MakeTest, UserResponse, UserTestAttempt

class QuestionSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Question
        fields = '__all__'


class MakeTestSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MakeTest
        fields = '__all__'

class UserTestAttemptSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserTestAttempt
        fields = '__all__'

class UserResponseSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserResponse
        fields = '__all__'