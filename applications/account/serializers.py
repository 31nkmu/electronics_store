from django.contrib.auth import get_user_model
from rest_framework import serializers
from applications.account import tasks

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, max_length=128, min_length=6, write_only=True)
    password_repeat = serializers.CharField(max_length=128, min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_repeat')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    @staticmethod
    def validate_phone_number(phone_number):
        if not phone_number.startswith('+996'):
            raise serializers.ValidationError('Ваш номер должен начинаться на +996')
        if len(phone_number) != 13:
            raise serializers.ValidationError('Некоректный номер телефона')
        return phone_number

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            password=validated_data['password'],
            email=validated_data['email'],
            is_active=validated_data['is_active'],
            codeword=validated_data['codeword'],
            phone_number=validated_data['phone_number']
        )
        code = user.activation_code
        tasks.send_user_activation_link.delay(user.email, code)
        return user