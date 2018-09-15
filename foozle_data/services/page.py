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
        "actions": [page_data["actions"]],
        "meta_data": page_data["metaData"],
        "enviroment": page_data["enviroment"],
        "data": page_data["page"],
        "unique_id": page_data["pageToken"],
    })
