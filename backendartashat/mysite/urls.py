from django.urls import path
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.SimpleRouter()
router.register('events', EventView)
router.register('courses', CourseView)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('comments/', CommentView.as_view()),
    path('teachers/', TeacherView.as_view()),
    path('total-info/', TotalInfoView.as_view()),
    path('material/<slug:course_name>/', MaterialView.as_view()),
    path('token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('token-logout/', Logout.as_view()),
] + router.urls