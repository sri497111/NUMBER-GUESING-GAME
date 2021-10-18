import sys
from time import sleep
from playsound import playsound

words = "starting NUMBER GUESSING GAME...\n"
print("""
controls, commands and rules
type your answer to get a fanfare/disapproval depending on your answer.
answers must only be integers/numbers or else you'll get an error.*
guessing game was only made for a little timelapse in your GOOD DAY.
thank you :)
if you want to QUIT, type in a ALPHABET instead, It'll throw an error.*
* send an email if game source wants to be changed, send the new source by email and DO NOT change the source on Github. 
this email is only for request.
EMAIL: sricharan.athanti@gmail.com    
         - sricharan



""")
for char in words:
                sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()
def guess():
            import random
            
            answer = (random.randint(1,10))
            change = (random.randint(1,3))
            change2 = (random.randint(1,3))
            a = (answer-change)
            b = (answer+change)
            print(f'my number is between {a} and {b}')
            guess = int(input("The number is "))
            if answer == guess:
                print("""                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                              congratulations you are
                                      correct
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
            else:
                print(f"""                        ------------------------------------
                              You are wrong try again
                                the number was {answer}
                        -------------------------------------""")

            from time import sleep
            import sys
            words = "Genarating new level...\n"
            for char in words:
                sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()
            
while guess:
      guess()