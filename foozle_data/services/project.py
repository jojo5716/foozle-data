from django.core.exceptions import ValidationError

from ..apps.data.models import Project

def get_project_by_uuid(project_uuid):
    """ 
    Return a project object by a uuid

    Args:
        project_uuid: {string} UUID

    Return:
        Instance of Project model
    """
    try:
        project = Project.objects.get(unique_id=project_uuid)
    except (ValidationError, Project.DoesNotExist):
        project = None
    
    return project
