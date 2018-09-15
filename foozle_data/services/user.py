from ..apps.data.models import UserProfile


def get_or_create(user_id, user_data={}):
    """ 
    Return a user object by a session id

    Args:
        user_id: {string} UUID

    Return:
        Tuple of two elements (obj, created|bool)
    """
    return UserProfile.objects.get_or_create(
    unique_id=user_id,
    defaults={'data': user_data},
)
