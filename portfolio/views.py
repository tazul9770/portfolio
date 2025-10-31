from rest_framework.response import Response
from portfolio.models import Project, Skill, Contact
from rest_framework.viewsets import ModelViewSet
from portfolio.serializer import ProjectSerializer, SkillSerializer, ContactSerializer
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Send welcome email to the user
            user_email = serializer.data['email']
            user_msg = serializer.data['comment']

            send_mail(
                subject='Welcome to My Portfolio!',
                message='Thank you for reaching out! I will get back to you shortly.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_email],
                fail_silently=False,
            )

            send_mail(
                subject="My portfolio",
                message=f"{user_email} send you message\n\n{user_msg}",
                from_email=user_email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

