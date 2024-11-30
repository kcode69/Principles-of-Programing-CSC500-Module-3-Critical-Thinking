#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
#Write a Python program to solve the general version of the above problem. 
#Ask the user for the time now (in hours) and then ask for the number of hours to wait for 
# the alarm. Your program should output what the time will be on a 24-hour clock when the alarm goes off.

#pseudo-code: 
#Input the current time in HH:MM format, then while loop to check format of entry.
#Print the current time 
#Input time from now for alarm in HH:MM format
#check format of alarm minutes is less than 60 with while
#print when alarm will go off from now
#if sum of current minutes and alarm minutes is 60 or greater, adjust hour
#adjust alarm time hour to report alarm time in 24 time using %
#sum current minute and alarm minute
#print alarm hour and alarm minute in 24 hr time

#current time input in 24 hr and minute format
current_time = input("Enter time 24 hr format HH:MM\n")

#seperate hour and minute into variables hour
current_hour, current_min = [int(i) for i in current_time.split(":")]

#correct input if not in HH:MM format
while current_hour >= 24 or current_min >= 60:

    #current time input in 24 hr and minute format
    current_time = input("Enter time 24 hr format HH:MM\n")

    #seperate hour and minute into variables hour
    current_hour, current_min = [int(i) for i in current_time.split(":")]

#print current time
print("The time now is", current_hour, "hours and", current_min, "minutes")

#input time from now for alarm
time_from_now = input("Enter the amount of time from now for alarm \nin 24 hr format HH:MM\n")

time_from_now_hour, time_from_now_min = [int(i) for i in time_from_now.split(":")]

#check format of minutes for greater than 60
while time_from_now_min >= 60:
    time_from_now = input("Enter the amount of time from now for alarm \nin 24 hr format HH:MM\n")
    time_from_now_hour, time_from_now_min = [int(i) for i in time_from_now.split(":")]

#print when alarm will go off
print("An alarm will go off ", time_from_now_hour, "hours and ", time_from_now_min, "minutes from now")

#adjust hours if sum of current min and time from now min is equal greater than 60
if time_from_now_min + current_min >= 60:
    time_from_now_hour = time_from_now_hour + 1
    time_from_now_min = time_from_now_min - 60

#set time from now minute and hour based on 24 hr time
time_from_now_hour = (time_from_now_hour + current_hour) % 24
time_from_now_min = time_from_now_min + current_min

#print what time of day alarm will go off in 24 hr time
print("Alarm set for",time_from_now_hour,"hours and",time_from_now_min,"minutes")