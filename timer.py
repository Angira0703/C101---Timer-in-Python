import time

#Asking user input for time in seconds.
seconds = int(input("Enter time in number of seconds: "))

#defining the countdown timer function.
def countdown_timer(seconds):
    
    while seconds:

        minutes = int(seconds/60)
        seconds = int(seconds%60)
        timer_value = f"{minutes} : {seconds}"
        print(timer_value, end='\r')
        time.sleep(1)
        seconds-=1
    print("Timer ran out!")


#function calling
countdown_timer(int(seconds))

