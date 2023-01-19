from django.db.models import Avg
from rest_framework import serializers

from applications.electronics.models import Image, Electronic
from applications.feedback.models import Comment, Rating, Like
from applications.feedback.serializers import CommentSerializer
from applications.feedback.services import is_fan, is_reviewer, is_commented, is_favorite


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ElectronicSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Electronic
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        category = validated_data.pop('category')
        electronic = Electronic.objects.create(**validated_data)
        electronic.category.set(category)
        files = request.FILES
        for image in files.getlist('images'):
            Image.objects.create(electronic=electronic, image=image)
        return electronic

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get('request').user
        images = []
        for i in rep['images']:
            images.append(i['image'])
        rep['images'] = images
        rep['likes'] = Like.objects.filter(electronic=instance, like=True).count()
        rating = Rating.objects.filter(electronic=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            rep['rating'] = rating
        else:
            rep['rating'] = 0
        comments = Comment.objects.filter(electronic=instance)
        comments = CommentSerializer(comments, many=True).data
        comments = [{'user': i['user'], 'comment': i['comment']} for i in comments]
        rep['comments'] = comments
        rep['is_fan'] = is_fan(user=user, obj=instance)
        rep['is_reviewer'] = is_reviewer(user=user, obj=instance)
        rep['is_commented'] = is_commented(user=user, obj=instance)
        rep['is_favorite'] = is_favorite(user=user, obj=instance)
        return rep
