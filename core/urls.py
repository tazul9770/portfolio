from django.urls import path, include
from rest_framework_nested import routers
from portfolio.views import ProjectViewSet, SkillViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('skills', SkillViewSet, basename='skills')
router.register('contact', ContactViewSet, basename='contacts')

urlpatterns = [
    path('', include(router.urls))
]
