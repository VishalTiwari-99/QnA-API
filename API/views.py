from django.shortcuts import render
from rest_framework import viewsets
from .models import Question, TestSlot, UserResponse, UserTestAttempt
from .serializers import QuestionSerializers, TestSlotSerializers, UserTestAttemptSerializers
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class QuestionViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers

class TestSlotViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = TestSlot.objects.all()
    serializer_class = TestSlotSerializers

class UserTestAttemptViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = UserTestAttempt.objects.all()
    serializer_class = UserTestAttemptSerializers