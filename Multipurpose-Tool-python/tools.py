import cs50
import random
from colorama import init, Fore
import os
import datetime


#some formulas taken from http://pythonfiddle.com/

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def fas(value):
    """Formats value."""
    return "{:,.2f}".format(value)
    
def factorial(n):
    if n<0:
        return None
    elif n<2:
        return n
    else:
        return n*factorial(n-1)

def combin(n,k):
    return factorial(n)/factorial(n-k)

def permut(n,k):
    return combin(n,k)/factorial(k)

#print factorial(5), combin(33,6), permut(33,6)

def greatest_common_divisor(x,y):
    #print ("For", x, "and", y,",")
    r=x%y
    while r>0:
        r=x%y
        if r ==0: 
            #print ("the greatest common divisor is", y,".")
            print (y)
        else:
            q=y
            x=q
            y=r
#greatest_common_divisor(1071,1029)
    
class print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            #print(s1)
        #print('\n')

print_format_table()


def vowel_remover(text):
    string = ""
    for l in text:
        if l.lower() != "a" and l.lower() != "e" and l.lower() != "i" and l.lower() != "o" and l.lower() != "u":
            string += l
    return string

def clock_angle(h, m):
    h_deg = (h * 30) % 360
    m_deg = (m * 6) % 360
    h_deg += m / 2        # hr moves 30 degrees per 60 minutes
    angle = abs(h_deg - m_deg)
    if angle > 180:
        angle = 360 - angle
    return angle
    
#################
def generate_random_password(total, sequences):
    r = _generate_random_number_for_each_sequence(total, len(sequences))

    password = []
    for (population, k) in zip(sequences, r):
        n = 0
        while n < k:
            position = random.randint(0, len(population)-1)
            password += population[position]
            n += 1
    random.shuffle(password)
    
    while _is_repeating(password):
        random.shuffle(password)
        
    return ''.join(password)

def _generate_random_number_for_each_sequence(total, sequence_number):
    """ Generate random sequence with numbers (greater than 0).
        The number of items equals to 'sequence_number' and
        the total number of items equals to 'total'
    """
    current_total = 0
    r = []
    for n in range(sequence_number-1, 0, -1):
        current = random.randint(1, total - current_total - n)
        current_total += current
        r.append(current)
    r.append(total - sum(r))
    random.shuffle(r)

    return r

def _is_repeating(password):
    """ Check if there is any 2 characters repeating consecutively """
    n = 1
    while n < len(password):
        if password[n] == password[n-1]:
            return True
        n += 1
    return False
#############

def main():
    
    list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for list in list_of_lists:
            print (list)
            
    
    numbes = random.sample(range(1, 9), 8)
    print(numbes, sep='\t')
    
    numbes = [str(i) for i in numbes]
    
    width, height = 9, 9
    coordinates = [(x, y) for x in range(width) for y in range(height)]
    #print(coordinates)
    for x in range(3):
            print ("\t".join(numbes[(x*3):(x*3+3)]))

    
    person = input(bcolors.HEADER + 'Enter your full name: ' + bcolors.ENDC)
    if not person[0].isalpha():
        print("must be letters!")
        return 0
    #print("So simply we will call you: " +person[0].upper(), end=".")
    print(bcolors.HEADER + 'So simply we will call you: ' + bcolors.OKGREEN + person[0].upper(), bcolors.ENDC, end=".")
    leng = len(person)
    if person:
        for i in range(leng):
            if person[i] == ' ':
                #print(person[i+1].upper(), end=".")
                print(bcolors.OKGREEN + person[i+1].upper(), end="." + bcolors.ENDC)
    print()
    
    #print("Wanna play a couple of games?")
    #print('Press "1" to play a shoegame or Press "2" to play number guessing game or Press "3" to find the treasure!')
    #print('Press 0 to exit')
    print('\x1b[1;30;47m'+ bcolors.BOLD +'\t\t\t' + 'WANNA PLAY SOME GAMES?'.center(48) + '\x1b[0m', end="")
    now = datetime.datetime.now()
    print ('\t\t\t\t  ' + now.strftime("%Y-%m-%d %H:%M:%S %A"))
    print('\x1b[ 1;33;4m'+ bcolors.BOLD +'\t\t\t  '+ 'If you wanna see something colorful' + '\x1b[0m', end="")
    print (bcolors.BOLD + Fore.RED + ' P ' + Fore.YELLOW + 'R ' + Fore.GREEN + 'E ' + Fore.BLUE + 'S ' + Fore.MAGENTA + 'S ' + Fore.YELLOW + '"G"' + Fore.RESET)
    print('\x1b[1;36;45m'+ bcolors.BOLD +'\t\t\t'+ 'To Generate Random Password Press `PASS`'.center(48) + '\x1b[0m')
    print('\x1b[1;36;44m'+ bcolors.BOLD +'\t\t\t'+ 'To Take Some Notes Press `NOTE`'.center(48) + '\x1b[0m')
    print('\x1b[5;37;45m'+ bcolors.BOLD +'\t\t\t'+ 'No VOWELS `5`'.center(48) + '\x1b[0m')
    print('\x1b[1;36;44m'+ bcolors.BOLD +'\t\t\t'+ 'GUESS THE NUMBER `GUESSS`'.center(48) + '\x1b[0m')
    print('\x1b[1;33;45m'+ bcolors.BOLD +'\t\t\t\t'+ 'BIRTHDAY STATISTICS ' + '\x1b[0m', end="")
    print('\x1b[1;32;41m'+bcolors.BOLD+'` B'+'\x1b[0m'+'\x1b[1;33;41m'+bcolors.BOLD+'D'+'\x1b[0m'+'\x1b[1;36;41m'+bcolors.BOLD+'A'+'\x1b[0m'+'\x1b[1;37;41m'+bcolors.BOLD+'Y `'+'\x1b[0m')
    print('\x1b[1;36;44m'+ bcolors.BOLD +'\t\t\t'+ 'FIND GAME `F`'.center(48) + '\x1b[0m')    
    print('\x1b[5;37;45m'+ bcolors.BOLD + 'Press "1" to play a shoegame' + ' or ' + 'Press "2" to play number guessing game' + ' or ' + 'Press "3" to find the treasure!' + '\x1b[0m', end="   ")
    print('\x1b[5;37;41m'+ bcolors.BOLD + 'Press 0 to exit' + '\x1b[0m')
    #mathematics
    print (bcolors.BOLD +'\t\t\t    ' + Fore.YELLOW + ' "M" ' + Fore.MAGENTA + '  F ' + Fore.GREEN + 'O ' + Fore.BLUE + 'R'\
    + bcolors.BOLD + Fore.RED + '   M ' + Fore.YELLOW + 'A ' + Fore.GREEN + 'T ' + Fore.BLUE + 'H ' + Fore.MAGENTA + 'E ' + Fore.RED + 'M'\
    + Fore.RED + ' A ' + Fore.YELLOW + 'T ' + Fore.GREEN + 'I ' + Fore.BLUE + 'C ' + Fore.MAGENTA + 'S ' + Fore.RED + '!!' + Fore.RESET)    
    game = input("")
    #if game ==("5"):
        #print(print_format_table(s1))
    
    if game==("5"):
        text=input("fuck off: ")
        print (vowel_remover(text))
    
    if game ==("m"):
        print (bcolors.BOLD + Fore.RED + 'FACTORIAL "1", ' + Fore.YELLOW + 'COMBINATION "2", ' + Fore.GREEN + 'PERMUTATION "3", ' + Fore.BLUE + 'EXAM CALCULATION "4", '+ Fore.MAGENTA + 'CELCIUS - FAHREINHEIT "5", ' + Fore.GREEN + 'RANDOM CLOCK ANGLES "6", '+ Fore.YELLOW + 'GREATEST COMMON DIVISOR "2"' +Fore.RESET)
        math = input("")
        
        if math==("1"):
            n = input(bcolors.OKBLUE + 'Number: ' + bcolors.ENDC)
            n=int(n)
            print(bcolors.FAIL + 'Result: ' + bcolors.ENDC, end="")
            print (factorial(n))
        
        if math==("2"):
            n = input(bcolors.OKBLUE + 'Number(1): ' + bcolors.ENDC)
            k = input(bcolors.OKBLUE + 'Number(2): ' + bcolors.ENDC)
            n= int(n)
            k= int(k)
            print(bcolors.FAIL + 'Result: ' + bcolors.ENDC, end="")
            print(combin(n,k))
        
        if math==("3"):
            n = input(bcolors.OKBLUE + 'Number(1): ' + bcolors.ENDC)
            k = input(bcolors.OKBLUE + 'Number(2): ' + bcolors.ENDC)
            n= int(n)
            k= int(k)
            print(bcolors.FAIL + 'Result: ' + bcolors.ENDC, end="")
            print(permut(n,k))
            
        if math ==("4"):
            #numberofTest, average, grade, scoreEntered
            grade = 0
            numberofTest = 0
            average = 0
            while True:
                print("Number of Tests: {:,.0f} ".format(numberofTest), end="")
                print("Average: {:,.2f}".format(average))
                #print("Test Sayisi: %.0f, Ortalama: %.2f", numberofTest, average)
                scoreEntered = input(bcolors.OKBLUE + 'Exam Grade: ' + bcolors.ENDC)
                scoreEntered = int(scoreEntered)
                if scoreEntered > 100:
                    print("Cannot be accepted 100 or more")
                    break
                grade += scoreEntered
                numberofTest+=1
                average = grade / numberofTest
                if (average > 70):
                        print('\x1b[1;37;42m' + 'Good Job!' + '\x1b[0m')
                        continue
                if (average <= 50):
                        print('\x1b[1;37;41m' + 'You need to work more!' + '\x1b[0m')
                        continue
                if (average < 70 and average > 50):
                        print('\x1b[1;37;43m' + 'That`s OK!' + '\x1b[0m')
                        continue
                while not scoreEntered:
                    return 0
        
        if math==("5"):
            #Celsius = int(input("Enter a temperature in Celsius: "))
            Celsius = int(input(bcolors.HEADER + 'Enter a temperature in Celsius: ' + bcolors.ENDC))
            Fahrenheit = 9.0/5.0 * Celsius + 32
            print (Fore.RED, bcolors.BOLD, "Temperature:", Fore.RESET, fas(Celsius), "°C", Fore.GREEN, "=", Fore.RESET, fas(Fahrenheit), "°F")
        
        if math==("6"):
            print(('\x1b[1;37;46m' + 'If you want 5 random clock angles PRESS `1`, or continue with custom clock PRESS `2`' + '\x1b[0m'))
            clock = input("")
            #print ("The smallest angle at %d:%02d is %d degrees" % (12, 0, clock_angle(12, 0)))
            #print ("The smallest angle at %d:%02d is %d degrees" % (3, 15, clock_angle(3, 15)))
            #print ("The smallest angle at %d:%02d is %d degrees" % (6, 0, clock_angle(6, 0)))
            if clock==("1"):
                print(bcolors.WARNING + "Five Random Test Cases" + bcolors.ENDC)
                for x in range(5):
                    h, m = int(12*random.random())+1, int(60*random.random())
                    print (bcolors.BOLD, "The smallest angle at", Fore.GREEN, "%d:%02d" " is " "%d degrees" % (h, m, clock_angle(h, m)), Fore.RESET)
            if clock==("2"):
                h = input(bcolors.WARNING + "Hour Hand: " + bcolors.ENDC)
                m = input(bcolors.WARNING + "Minute Hand: " + bcolors.ENDC)
                h, m = int(h), int(m)
                if (m>59 or m<0) or (h>12 or h<0):
                    print(bcolors.FAIL+ bcolors.BOLD + "Hour must be in 0-12 and minute must be in 0-59 range." + bcolors.ENDC)
                    return
                print (bcolors.BOLD, "The smallest angle at", Fore.GREEN, "%d:%02d" " is " "%d degrees" % (h, m, clock_angle(h, m)), Fore.RESET)
     
        if math==("7"):
            x = input(bcolors.OKBLUE+ "First Number: "+bcolors.ENDC)
            y = input(bcolors.OKBLUE+"Second Number: "+bcolors.ENDC)
            x,y = int(x), int(y)
            if x == y:
                print(bcolors.WARNING, "the greatest common divisor is:", bcolors.ENDC, y)
            print(bcolors.WARNING, "the greatest common divisor of",'\x1b[1;37;44m', "{}".format(x) ,'\x1b[0m',"and",'\x1b[1;37;44m', "{}".format(y),'\x1b[0m' " is:", bcolors.ENDC, bcolors.OKGREEN, end="")
            print(greatest_common_divisor(x,y))
        
            
    if game ==("g"):
        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')
    
    if game ==("0"):
        return exit
    
    if game ==("1"):
        #shoe= input('Enter your shoe number: ')
        shoe = input('\x1b[1;37;44m' + 'Enter your shoe number: ' + '\x1b[0m')
        shoe = int(shoe)
        shoe = (((shoe*5)+50)*20)+1017
        #year= input('birthday: ')
        year= input('\x1b[1;37;44m' + 'Your Birthday: ' + '\x1b[0m')
        year = int(year)
        year = year-shoe
        #print(year)
        year = str(year)
        print('\x1b[1;30;47m'+ 'Result: ' + year + '\x1b[0m')
    
    if game ==("2"):
        #print("[P1] = Player1 // [P2] = Player2")
        #print("All numbers must 6 digits")
        #print (bcolors.WARNING + '\t' + "[P1] = Player1 // [P2] = Player2" + bcolors.ENDC)
        print(bcolors.OKGREEN + '\t' + "[P1] = Player1 " + bcolors.ENDC, end="")
        print(bcolors.FAIL + "||" + bcolors.BOLD, end="")
        print(bcolors.OKBLUE + " [P2] = Player2" + bcolors.ENDC)
        print (bcolors.WARNING + "\t   " + bcolors.UNDERLINE + "All numbers must 6 digits!" + bcolors.ENDC)
        #n1 = input('[P1] First number: ')
        n1 = input(bcolors.OKGREEN + "[P1] First number: " + bcolors.ENDC)
        if len(n1)>6 or len(n1)<6:
            print("must be 6 digits no less, no more")
            return 0
        n1 = int(n1)
        sonuc = n1 + 1999998
        #print("Guess: ", end="")
        sonuc = str(sonuc)
        print('\x1b[1;36;41m' + 'MY GUESS: ' + sonuc + '\x1b[0m')
        #print(sonuc)
        #n2 = input('[P2] Second number: ')
        n2 = input(bcolors.OKBLUE + "[P2] Second number: " + bcolors.ENDC)
        n2 = int(n2)
        #n3 = input('[P1] Third number: ')
        n3 = input(bcolors.OKGREEN + "[P1] First number: " + bcolors.ENDC)
        n3 = int(n3)
        #n4 = input('[P2] Forth number: ')
        n4 = input(bcolors.OKBLUE + "[P2] First number: " + bcolors.ENDC)
        n4 = int(n4)
        #n5 = input('[P1] Fifth number: ')
        n5 = input(bcolors.OKGREEN + "[P1] First number: " + bcolors.ENDC)
        n5 = int(n5)
        sonuc2 = n1+n2+n3+n4+n5
        sonuc2 = str(sonuc2)
        print('\x1b[1;36;41m' + 'RESULT FOUND: ' + sonuc2 + '\x1b[0m')
        #print("Result found: ", end="")
        #print(sonuc2)
        
    if game ==("3"):
        x,y = 0,0
        while not (x,y)==(3,4):
            #path = input("Which Way: ")
            path = input('\x1b[1;33;45m' + 'Which Way: ' + '\x1b[0m')
            if (x>=4):
                #print("Go one step up!")
                print (bcolors.FAIL + "Go one step up!" + bcolors.ENDC)
            if (x<0):
                #print("Go one step down!")
                print (bcolors.FAIL + "Go one step down!" + bcolors.ENDC)
            if (y<0):
                #print("Go one step right!")
                print (bcolors.FAIL + "Go one step right!" + bcolors.ENDC)
            if (y>=5):
                #print("Go one step left!")
                print (bcolors.FAIL + "Go one step left!" + bcolors.ENDC)
            
            if path==("s"): 
                x+=1 
                print([x,y])
                continue
            if path==("d"):
                y+=1
                print([x,y])
                continue
            if path==("w"):
                x-=1
                print([x,y])
                continue
            if path==("a"):
                y-=1
                print([x,y])
                continue
        while (x,y)==(3,4):
            #print (bcolors.OKGREEN + "Congrats you get the shit!" + bcolors.ENDC)
            print('\x1b[1;37;42m' + 'Congrats you get the shit!' + '\x1b[0m')
            break
                
    if game ==("f"):
        data=[]
        yournumber = int(input('number: '))
        #yournumber = int(yournumber)
        a = input('Are You Ready! ')
        if a == ('yes'):
            for i in range(5):
                b = int(input('Number{}: '.format(i+1)))
                #b = int(b)
                data.append(b)
        if yournumber in data:
            print('found it bitch')
        if not yournumber in data:
            print('no chance mate')
        print (data)
        
    if game ==("note"):
        intake = input('Input: ')
        print ('would you like to save it?')
        a = input()
        if a == ('yes'):
            fname = input('File name: ')
            with open(fname+".txt", "a") as f:
                now = datetime.datetime.now()
                f.write((now.strftime("%Y-%m-%d %H:%M:%S %A" + " ( Noted )"))+ "\n" + intake + "\n" + '#'*150 + "\n")
        print(bcolors.WARNING +  "{}.txt created and saved.".format(fname) + bcolors.ENDC)
        #print (intake)
                
    if game ==("bday"):
        now = datetime.datetime.now()
        print (bcolors.HEADER + "Today's date: " + now.strftime("%d-%m-%Y") + bcolors.ENDC)
        nowday = now.strftime("%d")
        nowday = int(nowday)
        nowmonth = now.strftime("%m")
        nowmonth = int(nowmonth)
        nowyear = now.strftime("%Y")
        nowyear = int(nowyear)
        #print(nowday, nowmonth, nowyear)
        now = now.strftime("%d-%m-%Y")
        bday = input("Day: ")
        bday = int(bday)
        if bday > 31:
            print("error!")
            return 
        bmonth = input("Month: ")
        bmonth = int(bmonth)     
        if bmonth > 12:
            print("error!")
            return 
        byear = input("Year: ")
        byear = int(byear)
        if byear > nowyear:
            print("error!")
            return
        yy = nowyear-byear
        mm = nowmonth-bmonth
        dd = nowday-bday
        mmm = (abs(mm)*30)+dd
        yyy = ((abs(yy)*12)*30)+mmm
        print("\n"+ bcolors.WARNING + "STATISTICS" + bcolors.ENDC)
        print(fas(yyy) +" days past since you were born.")
        print(fas(yyy*24) +" hours past since you were born.")
        hours = yyy*24
        print(fas(hours*60) +" seconds past since you were born.")
        print(abs(dd), "days", abs(mm), "months", abs(yy), "years past..")
        if (nowmonth==bmonth) and (nowday==bday):
            #print(bcolors.OKGREEN + "HAPPY BIRTHDAY MOTHERFUCKER!" + bcolors.ENDC)
            print('\x1b[1;37;42m' + 'HAPPY BIRTHDAY MOTHERFUCKER!' + '\x1b[0m')
        else:
            print(bcolors.FAIL, abs(dd), "days", abs(mm), "months left until your birthday!", bcolors.ENDC)

    if game ==("pass"):
        LOWERCASE_CHARS = tuple(map(chr, range(ord('a'), ord('z')+1)))
        UPPERCASE_CHARS = tuple(map(chr, range(ord('A'), ord('Z')+1)))
        DIGITS = tuple(map(str, range(0, 10)))
        SPECIALS = ('!', '@', '#', '$', '%', '^', '&', '*')
        
        SEQUENCE = (LOWERCASE_CHARS,
                    UPPERCASE_CHARS,
                    DIGITS,
                    SPECIALS,
                    )
        print(bcolors.WARNING, "The Password below created with the following rules: ", bcolors.ENDC)
        print(bcolors.FAIL, "1.",bcolors.ENDC, "6-20 characters")
        print(bcolors.FAIL, "2.",bcolors.ENDC, "at least one uppercase character")
        print(bcolors.FAIL, "3.",bcolors.ENDC, "at least one lowercase character")
        print(bcolors.FAIL, "4.",bcolors.ENDC, "at least one digit")
        print(bcolors.FAIL, "5.",bcolors.ENDC, "at least one special character (!, @, #, $, %, ^, &, *)")
        print(bcolors.FAIL, "6.",bcolors.ENDC, "no more than 2 characters repeating consecutively")
        passw = []
        passw = (generate_random_password(random.randint(6, 30), SEQUENCE))
        print("The PASS: "+ '\x1b[1;37;42m' + passw + '\x1b[0m')
        fuk = input(bcolors.OKGREEN+ "To save the pass 2,"+bcolors.ENDC+ bcolors.FAIL+ " or to exit press '0'"+ bcolors.ENDC + "\n")
        if fuk ==("2"):
            fname = input(bcolors.OKBLUE + "File Name: " + bcolors.ENDC)
            with open(fname+".txt", "a") as f:
                now = datetime.datetime.now()
                f.write((now.strftime("%Y-%m-%d %H:%M:%S %A" + " ( Password )"))+ "\n" + passw + "\n" + '#'*150 + "\n")
                print(bcolors.WARNING +  "{}.txt created and saved.".format(fname) + bcolors.ENDC)
        if fuk ==("0"):
            return exit

        #fuk = input(bcolors.OKBLUE+ "  if you wanna change the file's name press 2,"+bcolors.ENDC+ bcolors.FAIL+ " or to exit press '0'"+ bcolors.ENDC + "\n")
        #if fuk ==("2"):
            #fn = input("file name: ")
            #os.rename("file.txt", fn)
        #if fuk ==("0"):
            #return exit
            
    if game ==("guess"):
        
        print (bcolors.BOLD + Fore.RED + 'GUESS GAME[1] `1`, ' + Fore.YELLOW + 'GUESS GAME[3] `2`, ' + Fore.GREEN + 'GUESS GAME[8]  `3`, '+Fore.RESET)
        guess = input("")
        
        if guess==("1"):
            number = int(input(bcolors.WARNING + "hold a number!: " + bcolors.ENDC))
            print('\x1b[1;31;47m' + 'RESULT WILL BE: 1' + '\x1b[0m')
            multi = int(input(bcolors.WARNING + "Multiple with 4 [{}*4]: ".format(number)+ bcolors.ENDC))
            add = int(input(bcolors.WARNING + "Plus 18 [{}+18]: ".format(multi)+ bcolors.ENDC))
            divide = int(input(bcolors.WARNING + "Divide by 2 [{}/2]: ".format(add)+ bcolors.ENDC))
            minus = int(input(bcolors.WARNING + "Minus 7 [{}-7]: ".format(divide)+ bcolors.ENDC))
            multed = int(input(bcolors.WARNING + "Multiple with 3 [{}*3]: ".format(minus)+ bcolors.ENDC))
            divided = int(input(bcolors.WARNING + "Divide by 6 [{}/6]: ".format(multed)+ bcolors.ENDC))
            minused = int(input(bcolors.WARNING + "Minus your first number [{}-{}]: ".format(divided, number)+ bcolors.ENDC))
            yoursonuc = minused
            sonuc = ((((((number*4)+18)/2)-7)*3)/6)-number
            print(bcolors.OKBLUE + "Your Answer: {}".format(yoursonuc) + bcolors.ENDC)
            if yoursonuc == sonuc:
                print(bcolors.OKGREEN + "SUCCESS!" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "FAIL!" + bcolors.ENDC)
                
        if guess==("2"):
            number = int(input(bcolors.WARNING + "hold a number!: " + bcolors.ENDC))
            print('\x1b[1;31;47m' + 'RESULT WILL BE: 5' + '\x1b[0m')
            multi = int(input(bcolors.WARNING + "Multiple with 2 [{}*2]: ".format(number)+ bcolors.ENDC))
            add = int(input(bcolors.WARNING + "Plus 10 [{}+10]: ".format(multi)+ bcolors.ENDC))
            divide = int(input(bcolors.WARNING + "Divide by 2 [{}/2]: ".format(add)+ bcolors.ENDC))
            minused = int(input(bcolors.WARNING + "Minus your first number [{}-{}]: ".format(divide, number)+ bcolors.ENDC))
            yoursonuc = minused
            sonuc = (((number*2)+10)/2)-number
            print(bcolors.OKBLUE + "Your Answer: {}".format(yoursonuc) + bcolors.ENDC)
            if yoursonuc == sonuc:
                print(bcolors.OKGREEN + "SUCCESS!" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "FAIL!" + bcolors.ENDC)
                
                
        if guess==("3"):
            number = int(input(bcolors.WARNING + "hold a number!: " + bcolors.ENDC))
            print('\x1b[1;31;47m' + 'RESULT WILL BE: 8' + '\x1b[0m')
            add = int(input(bcolors.WARNING + "Add it the next number [{}+{}]: ".format(number, number+1)+ bcolors.ENDC))
            added = int(input(bcolors.WARNING + "Plus 15 [{}+15]: ".format(add)+ bcolors.ENDC))
            divide = int(input(bcolors.WARNING + "Divide by 2 [{}/2]: ".format(added)+ bcolors.ENDC))
            minused = int(input(bcolors.WARNING + "Minus your first number [{}-{}]: ".format(divide, number)+ bcolors.ENDC))
            yoursonuc = minused
            sonuc = (((number+(number+1))+15)/2)-number
            print(bcolors.OKBLUE + "Your Answer: {}".format(yoursonuc) + bcolors.ENDC)
            if yoursonuc == sonuc:
                print(bcolors.OKGREEN + "SUCCESS!" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "FAIL!" + bcolors.ENDC)
        
        
if __name__ == "__main__":
    main()
    
