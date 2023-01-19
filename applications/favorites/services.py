from applications.favorites.models import Favorite
from applications.favorites.serializers import FavoriteSerializer


def add_del_favorite(obj, user):
    """
    Добавляет/удаляет `obj` из избранных
    :param obj: `obj` который добавляется
    :param user: пользователь который добавляет/удаляет
    """
    fav_obj, is_created = Favorite.objects.get_or_create(electronic=obj, user=user)
    fav_obj.is_favorite = not fav_obj.is_favorite
    fav_obj.save()
    if fav_obj.is_favorite:
        return 'Добавлено в избранное'
    return 'Удалено из избранных'


def is_favorite(obj, user):
    """
    Проверяет, находится ли `obj` в избранных у пользователя
    :param obj: electronic
    :param user: пользователь
    """
    try:
        return Favorite.objects.filter(electronic=obj, user=user, is_favorite=True).exists()
    except TypeError:
        return False


def get_favorites(user):
    """
    Выводит избранных список `obj`
    :param user: пользователь который добавил в избранное
    """
    try:
        electronic = Favorite.objects.filter(user=user, is_favorite=True)
        serializer = FavoriteSerializer(electronic, many=True)
        return serializer.data
    except TypeError:
        return []
