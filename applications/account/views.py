from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from applications.account import serializers

User = get_user_model()


class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
