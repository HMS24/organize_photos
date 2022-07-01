from datetime import datetime

def get_split_datetime(timestamp):
    try:
        (date, time) = str(datetime.fromtimestamp(timestamp)).split(' ')
    except ValueError:
        print('incorrect timestamp')

    return (*date.split('-'), *time.split(':'))
