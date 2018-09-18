from datetime import datetime


def convert_iso_string_date(iso_date):
    try:
        return datetime.strptime(iso_date, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        return datetime.now()