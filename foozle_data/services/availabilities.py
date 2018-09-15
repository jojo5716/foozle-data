from ..apps.data.models import Availability


def create(availability_data):
    """ 
    Return a user object by a session id

    Args:
        availability_data: {dict} Availability json

    Return:
        {Availability|None}: New instance of Availability model or None
    """
    if availability_data["availability"]:
        return Availability.objects.create(**{
            "hotel": {
                "code": availability_data["metaData"]["hotelCode"].strip(),
                "name": availability_data["metaData"]["hotelName"].strip(),
                "currency": availability_data["metaData"]["hotelCurrencyCode"]
            },
            "data": availability_data["availability"],
        })

