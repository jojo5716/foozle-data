from ..apps.data.models import Page


def create_page(page_data):
    """ 
    Return a new Page object

    Args:
        page_data: {dict} Dict with page data

    Return:
        Instance of Page model
    """
    return Page.objects.create(**{
        "meta_data": page_data["metaData"],
        "enviroment": page_data["enviroment"],
        "data": page_data["page"],
        "unique_id": page_data["pageToken"],
    })

def get_by_id(page_token):
    """ 
    Return a Page instance by a unique id field

    Args:
        page_token: {string} unique_id field into Page model

    Return:
        Instance of Page model
    """
    try:
        page = Page.objects.get(unique_id=page_token)
    except Page.DoesNotExist:
        page = None
    
    return page