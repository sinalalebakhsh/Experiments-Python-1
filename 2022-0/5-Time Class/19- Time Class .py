import os
os.system('cls')

class Time:
    def __init__(self, hour , minutes , second) :
        if hour > 24:
            raise ValueError(f'You can only select a hour between 0 and 24. not {hour} ') 
        if minutes > 60:
            raise ValueError(f'You can only select a minutes between 0 and 60. not {minutes} ')
        if second > 60:
            raise ValueError(f'You can only select a second between 0 and 60. not {second} ')
        self.hour = hour
        self.minutes = minutes
        self.second = second

    def __str__(self):
        return f'{self.hour:02}:{self.minutes:02}:{self.second:02}'

    def __add__(self, time_object):
        seconds = self.second + time_object.second
        minutes = self.minutes + time_object.minutes + (seconds // 60)
        hour = self.hour + time_object.hour + (minutes // 60)
        return Time(hour%24, minutes%60, seconds%60)

    def __gt__(self, time_object):
        self_object = self.second + (self.minutes * 60) + (self.hour * 60 ** 2)
        time_object = time_object.second + (time_object.minutes * 60) + (time_object.hour * 60 ** 2)
        return self_object > time_object

time1 = Time(22 , 1 , 1)

time2 = Time(20 , 59 , 59)

time3 = time1 + time2
print()
print(time1 > time2)
print()
print()



#==================================================================

# class A: pass

# a = dir(A)

# for s in a:
#     print(s)





        