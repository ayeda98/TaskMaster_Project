from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, GroupViewSet, GroupMembershipViewSet, CommentViewSet, UserCreate

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'group-memberships', GroupMembershipViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='user-create'),
]
