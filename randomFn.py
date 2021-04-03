import random #https://docs.python.org/3/library/random.html
import names #pip install names https://pypi.org/project/names/
import time
import datetime

def randInt(min,max): #min <= x <= max
    return random.randint(min,max)

def randName(): #generates a random name
    x = "female" if randInt(0,1) == 0 else "male"
    return names.get_full_name(x)

def random_date(start, end):
    def str_time_prop(start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)
        return time.strftime(format, time.localtime(ptime))
    prop = random.random()
    return str_time_prop(start, end, '%Y-%m-%d %I:%M:%S', prop)

def random_timestamp(x, today):
    res = []
    today = datetime.date.today()
    frmt = '%Y-%m-%d %I:%M:%S'
    d = 1 if today else 7
    start = (today-datetime.timedelta(days=d)).strftime(frmt)
    end = (today).strftime(frmt)

    for i in range(x):
        one = random_date(start, end)
        one = datetime.datetime.strptime(one,frmt)
        two = one+datetime.timedelta(hours=16)
        two = random_date(one.strftime(frmt), two.strftime(frmt))
        two = datetime.datetime.strptime(two, frmt)
        res.append([one,two])
        end = one.strftime(frmt)
        if d == 1:
            d = 7
            start = (today-datetime.timedelta(days=d)).strftime(frmt)
    return res

# res = random_timestamp(3)
# for i in range(3):
#     for j in range(2):
#         print(res[i][j])