import datetime



def DateAndTime():
    "This function print time and date"
    time = datetime.datetime.now().strftime("%I:%M:%S ")
    date = datetime.date.today()
    print(time)
    print(date)
DateAndTime()

def Letter(Name,Class,Rollnumber,k):
    "This function basically based on arguments"
    name = Name
    std = Class
    Rolln = Rollnumber
    kp= k
    print(' ')
    print(str(name))
    print(str(std))
    print(str(Rolln))



Letter('k' , 12,56,5)