from django.urls import include, path
from rest_framework import routers
from .views import QuestionViewset, TestSlotViewset, UserTestAttemptViewset

router = routers.DefaultRouter()
router.register('question',QuestionViewset, basename='question')
router.register('test-slot', TestSlotViewset, basename='testslot')
router.register('test-attempt', UserTestAttemptViewset, basename='testattempt')

urlpatterns = [
    path('', include(router.urls)),
]