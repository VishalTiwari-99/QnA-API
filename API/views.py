from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import Question, MakeTest, UserResponse, UserTestAttempt
from .serializers import QuestionSerializers, MakeTestSerializers, UserTestAttemptSerializers, UserResponseSerializers
from rest_framework.permissions import IsAuthenticated


class QuestionViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers

class MakeTestViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = MakeTest.objects.all()
    serializer_class = MakeTestSerializers

class UserTestAttemptViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = UserTestAttempt.objects.all()
    serializer_class = UserTestAttemptSerializers

# class UserResponseViewset(viewsets.ModelViewSet):
#     permission_class = [IsAuthenticated]
#     serializer_class = UserResponseSerializers
#     def get_queryset(self):
#         user = self.
#         return UserResponse.objects.filter(user=user, test=test_pk)

        

