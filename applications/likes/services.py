from applications.likes.models import Like
from applications.likes.serializers import FanSerializer


def like_unlike(user, obj):
    """
    Ставит и убирает лайк
    :param user: пользователь, который ставит лайк
    :param obj: `obj`, которому ставят лайк
    :return: статус: like/unlike
    """
    like_obj, is_created = Like.objects.get_or_create(user=user, electronic=obj)
    like_obj.like = not like_obj.like
    like_obj.save()
    if not like_obj.like:
        return 'unliked'
    return 'liked'


def is_fan(user, obj):
    """
    Проверяет поставил ли пользователь лайк
    :param user: пользователь, которого проверяем
    :param obj: `obj`, которому пользователь поставил лайк (или не поставил)
    """
    try:
        like = Like.objects.filter(user=user, electronic=obj)
        if like.exists() and like[0].like:
            return True
        return False
    except TypeError:
        return False


def get_fans(obj):
    """
    Выводит список пользователей, поставивших лайк
    :param obj: `obj` которому поставили лайк
    """
    fans = Like.objects.filter(electronic=obj, like=True)
    serializer = FanSerializer(fans, many=True)
    return serializer.data

