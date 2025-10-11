from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from portfolio.models import Project, Skill, Contact
from rest_framework.viewsets import ModelViewSet
from portfolio.serializer import ProjectSerializer, SkillSerializer, ContactSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

