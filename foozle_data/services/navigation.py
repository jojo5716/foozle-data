from ..apps.data.models import Navigation


def get_or_create(navigation_query, page):
    """ 
    Return a navigation object by a session

    Try to get a Navigation by a session id, if it does not exist,
    we create and return a new Navigation instance.

    Args:
        navigation_data: {dict} Dict with all navigation data
        user: {UserProfile} UserProfile instance

    Return:
        Instance of Navigation model
    """
    return Navigation.objects.get_or_create(
        session_id=navigation_query["session_id"],
        defaults=navigation_query,
    )


def register_page(navigation, page):
    navigation.page.add(page)