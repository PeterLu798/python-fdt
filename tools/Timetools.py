from _datetime import datetime
import tzlocal


def now():
    return datetime.now()


my_time_zone = tzlocal.get_localzone_name()
