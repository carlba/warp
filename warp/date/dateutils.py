from random import randrange
from datetime import timedelta
from datetime import datetime

def get_random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def get_iso_date_string(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def main():
    ten_days_back = datetime.now() - timedelta(days=10)
    ten_days_ahead = datetime.now() + timedelta(days=10)


    print get_random_date(ten_days_back,ten_days_ahead)

    print get_iso_date_string(datetime.now().replace(minute=0,second=0,microsecond=0))

    #print datetime(year=now.year,month=now.month,day=now.day,hour=now.hour, minute=now.minute,second =now.second, microsecond=now.microsecond)










if __name__ == '__main__':
    main()