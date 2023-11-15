from datetime import datetime

def Time():
    time = datetime.now().strftime("%I:%M:%S")
    print(time)

Time()