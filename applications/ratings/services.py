from rest_framework import serializers

from applications.ratings.models import Rating
from applications.ratings.serializers import ReviewerSerializer


def give_rating(obj, user, rating):
    """
    Ставит рейтинг
    :param obj: `obj` которому ставят рейтинг
    :param user: пользователь который ставит рейтинг
    :param rating: рейтинг который поставил пользователь
    """
    if 0 <= int(rating) <= 5:
        rating_obj, is_created = Rating.objects.get_or_create(user=user, electronic=obj)
        rating_obj.rating = rating
        rating_obj.save()
        if not is_created:
            return 'Рейтинг обновлен!'
        return 'Рейтинг создан!'
    raise serializers.ValidationError('Неверно введен рейтинг')


def del_rating(obj, user):
    """
    Удаляет рейтинг
    :param obj: рейтинг который удаляют
    :param user: пользователь который удаляет рейтинг
    """
    try:
        Rating.objects.get(electronic=obj, user=user).delete()
    except Rating.DoesNotExist:
        pass


def is_reviewer(obj, user):
    """
    Оставлял ли пользователь рейтинг
    :param obj: `obj` на который поставили рейтинг (или не поставили)
    :param user: пользователь который поставил рейтинг
    """
    try:
        return Rating.objects.filter(user=user, electronic=obj).exists()
    except TypeError:
        return False


def get_reviewers(obj):
    """
    Выводит список пользователей, поставивших рейтинг
    :param obj: `obj` которому поставили рейтинг
    """
    users = Rating.objects.filter(electronic=obj)
    serializer = ReviewerSerializer(users, many=True)
    return serializer.data
