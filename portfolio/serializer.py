from rest_framework import serializers
from portfolio.models import Project, Contact

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description',
                 'image', 'tech_stack', 'live_link',
                 'github_frontend_link', 'github_backend_link', 'created_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone_number', 'comment']

    def validate_phone_number(self, number):
        if not number.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits")
        if len(number) != 11:
            raise serializers.ValidationError("Phone number must be exactly 11 digits.")
        return number