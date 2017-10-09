from datetime import datetime
import webbrowser
from time import sleep
import random

"""
def seconds_elapsed(current,later):
    h1,m1,s1 = current.hour,current.minute,current.second
    h2,m2,s2 = later.hour,later.minute,later.second

    current_minutes = h1*60*60 + m1*60 + s1
    later_seconds = h2*60*60 + m2*60 + s2
    return(later_seconds-current_minutes)
"""
#colors
class bcolors:
    HEADER = '\x1b[1;34;43m'
    OKBLUE = '\x1b[1;37;44m'
    OKGREEN = '\x1b[1;37;42m'
    WARNING = '\x1b[1;37;41m'
    FAIL = '\x1b[5;37;40m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
#colortable    
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38): 
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')
#print_format_table()

print('Current Time: ' + datetime.now().strftime('%H:%M:%S / %A'))
date_format = '%H:%M:%S'
now = datetime.now().strftime('%H:%M:%S')
now = datetime.strptime(now,date_format).time()
alarm = input('Alarm Time(HH:MM (:SS is optional)): ')
print('\x1b[1;37;41m' + 'CLOCK IS SET TO ' + alarm + '\x1b[0m')
print(datetime.now().strftime('%H:%M:%S / %A'))
print('\x1b[2;37;40m' + 'GOOD NIGHT MOTHERFUCKER' + '\x1b[0m')

alarma = datetime.strptime(alarm, date_format).time()

alarm_hour = int(alarma.strftime('%H'))
alarm_minute = int(alarma.strftime('%M'))
alarm_second = int(alarma.strftime('%S'))
#print(alarm_hour, alarm_minute, alarm_second)
secsalarm = alarm_hour*60*60 + alarm_minute*60 + alarm_second
secsalarm = int(secsalarm)
#print(secsalarm)

now = datetime.now()
nowhour = int(now.strftime("%H"))
nowminute = int(now.strftime("%M"))
nowsecs = int(now.strftime("%S"))

#getting the hours/minutes/left thing
#print(nowhour, nowminute)
if (now.strftime("%H") == '00' and alarm_minute < nowminute) or (now.strftime("%H") == '12' and alarm_minute < nowminute):
    nowhour += 1
if (alarm_second < nowsecs) or (alarm_minute < nowminute):
    alarm_minute = (60 - nowminute) + alarm_minute
    if alarm_minute > 60:
        alarm_minute -= 60
    if alarm_second < nowsecs:
        alarm_second = (60 - nowsecs) + alarm_second
        alarm_minute -= 1
    print(alarm_hour - nowhour, 'hours', alarm_minute, 'minutes', alarm_second, 'seconds left!')
else:
    print(alarm_hour - nowhour, 'hours', alarm_minute - nowminute, 'minutes', alarm_second - nowsecs, 'seconds left!')
    
#depends on upper if condition
alarm_hours = int(alarma.strftime('%H'))
alarm_minutes = int(alarma.strftime('%M'))
alarm_seconds = int(alarma.strftime('%S'))
secsalarms = alarm_hours*60*60 + alarm_minutes*60 + alarm_seconds
nowhours = int(now.strftime("%H"))
nowminutes = int(now.strftime("%M"))
nowsecss = int(now.strftime("%S"))
secsnows= nowhours*60*60 + nowminutes*60 + nowsecss
print('\x1b[7;30;47m' + 'Total' + '\x1b[0m' + bcolors.HEADER, secsalarms - secsnows, '\x1b[0m' + '\x1b[7;30;47m' + 'seconds left!' + '\x1b[0m')
sleeptime = secsalarms - secsnows
#first try
"""
secsnow = nowhour*60*60 + nowminute*60 + nowsecs
print (nowhour, nowminute, nowsecs)
secsnow = int(secsnow)
#print(secsnow)
print('\x1b[7;30;47m' + 'Total' + '\x1b[0m' + bcolors.HEADER, secsalarm - secsnow, '\x1b[0m' + '\x1b[7;30;47m' + 'seconds left!' + '\x1b[0m')
"""

sleep(sleeptime)
while True:
    if (alarm == datetime.now().strftime('%H:%M')) or (alarm == datetime.now().strftime('%H:%M:%S')):
    #if alarm == datetime.now().strftime('%H:%M:%S'):
        for i in range(5):
            print('\x1b[6;30;42m' + 'WAKE THE FUCK UP!' + '\x1b[0m')
        f = open("alarm_urls.txt","r")
        songs = f.readlines()
        song_index = random.randint(0,2)
        webbrowser.open(songs[song_index])
        sleep(1)
        f.close()
        break
