from django.urls import include, path
from rest_framework import routers
from .views import QuestionViewset, MakeTestViewset, UserTestAttemptViewset

router = routers.DefaultRouter()
router.register('question',QuestionViewset, basename='question')
router.register('make-test', MakeTestViewset, basename='maketest')
router.register('test-attempt', UserTestAttemptViewset, basename='testattempt')

urlpatterns = [
    path('', include(router.urls)),
]