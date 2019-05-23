import datetime
from datetime import timedelta

if __name__ == '__main__':

    now = None
    for x in range(1,10):
        if now is None:
            now = datetime.datetime.now()
        else:
            now += timedelta(seconds=60)

        print(now)
