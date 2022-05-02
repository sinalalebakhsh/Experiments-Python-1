import os
os.system('cls')

class Time:
    def __init__(self, hour , minutes , second) :
        self.hour = hour
        self.minutes = minutes
        self.second = second
        if self.hour <= 23 and self.hour >= 0:
            if self.minutes <= 59:
                if self.second <= 59:
                    print('The amount of hours was correct.')
                    print()
                    print(f'{self.hour:02d}:{self.minutes:02d}:{self.second:02d}')

                else:
                    print('The value entered per second is incorrect.')
                    print()
                    print(self.second)
            else:
                print('The amount of minutes entered is incorrect.')
                print()
                print(self.minutes)    
        else:
            print('The value of the clock input is incorrect.')
            print()
            print(self.hour)

    def __str__(self):
        return f'{self.hour}:{self.minutes}:{self.second}'

    def __multiply__(self):
        return self.hour , self.minutes , self.second
        

time1 = Time(9,59,59)

time2 = Time(20,2,13)






        