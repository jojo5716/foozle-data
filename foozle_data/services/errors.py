from ..apps.errors.models import Error, ErrorDetail, ConsoleError, Network
from ..helpers import date as date_helper


def update_or_create(error_data):
    """ 
    Return a user object by a session id

    Args:
        error_data: {dict} error data (file error, message)

    Return:
        Tuple of two elements (obj, created|bool)
    """
    try:
        error = Error.objects.get(**error_data)
    except Error.DoesNotExist:
        error = Error(**error_data)
    else:
        error.issues += 1

    error.save()

    return error
        

def create_error_detail(detail_data):
    return ErrorDetail.objects.create(**{
        "type_name": detail_data["entry"],
        "line": detail_data["line"],
        # consoles = models.ManyToManyField(ConsoleError)
        # networks = models.ManyToManyField(Network)
        "url": detail_data["url"],
        "foozle_version": detail_data["version"],
        "meta_data": detail_data["metadata"],
    })

def create_console_log(console_data):
    return ConsoleError.objects.create(**{
        "type_console": console_data["severity"],
        "message": console_data["message"],
        "timeStamp": date_helper.convert_iso_string_date(console_data["timestamp"])
       
    })

def create_network_log(console_data):
    return Network.objects.create(**{
        "status": console_data.get("statusCode"),
        "method": console_data.get("method"),
        "url": console_data.get("url"),
        "startedOn": date_helper.convert_iso_string_date(console_data.get("startedOn")),
        "completedOn": date_helper.convert_iso_string_date(console_data.get("completedOn"))
       
    })