from rest_framework import serializers
from portfolio.models import Project, Skill, Contact

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description',
                 'image', 'tech_stack', 'live_link',
                 'github_frontend_link', 'github_backend_link', 'created_at']
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone_number', 'comment']