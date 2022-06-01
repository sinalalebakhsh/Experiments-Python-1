import os
from this import s
os.system('cls')

class Time:
    def __init__(self, hour , minutes , second) :
        if hour >= 24:
            raise ValueError(f'You can only select a hour between 0 and 23. not {hour} ') 
        if minutes >= 60:
            raise ValueError(f'You can only select a minutes between 0 and 59. not {minutes} ')
        if second >= 60:
            raise ValueError(f'You can only select a second between 0 and 59. not {second} ')
        self.hour = hour
        self.minutes = minutes
        self.second = second

    def __str__(self):
        return f'{self.hour:02}:{self.minutes:02}:{self.second:02}'

    def __add__(self, time_object):

        over_one_hour = (self.hour + time_object.hour)
        over_one_minutes = (self.minutes + time_object.minutes)
        over_one_second = (self.second + time_object.second)

                    
        
        return f'----{over_one_hour}:{over_one_minutes}:{over_one_second}'  

time1 = Time(23 , 59 , 59)

# time2 = Time(23 , 59 , 59)

# time3 = time1 + time2

time4 = Time(0, 0, 1) + time1 

# time3 += time4
print()
print()
# print(time3)
print()
print(time4)
print()



#==================================================================

# class A: pass

# a = dir(A)

# for s in a:
#     print(s)





        