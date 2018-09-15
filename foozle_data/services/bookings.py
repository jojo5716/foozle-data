from ..apps.data.models import Booking


def get_and_update(booking_data):
    """ 
    Return a booking object by a code

    If booking exist, then we will update if is necessary

    Args:
        navigation_data: {dict} Dict with all navigation data
        booking: {dict} Booking data

    Return:
        Instance of Booking model
    """
    try:
        booking = Booking.objects.get(code=booking_data["code"])
    except (Booking.DoesNotExist, KeyError):
        booking = None
    else:
        booking.data = booking_data
        booking.save()

    return booking
    