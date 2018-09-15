from ..apps.data.models import Action


def create(action_data, page):
    """ 
    Return a new Page object

    Args:
        action_data: {dict} Dict with action data
        page: {Page} Page model instance

    Return:
        Instance of Action model
    """
    return Action.objects.create(**{
        "action": action_data,
        "page": page
    })
