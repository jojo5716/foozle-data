from ..apps.data.models import Booking


def create_or_update(booking_data):
    """ 
    Return a booking object by a code

    If booking exist, then we will update if is necessary

    Args:
        navigation_data: {dict} Dict with all navigation data
        booking: {dict} Booking data

    Return:
        Instance of Booking model
    """
    booking = None

    if booking_data:        
        try:
            booking = Booking.objects.get(code=booking_data["bookingCode"])
        except (Booking.DoesNotExist, KeyError):
            booking = Booking(code=booking_data["bookingCode"])
        
        booking.data = booking_data
        booking.save()

    return booking
    