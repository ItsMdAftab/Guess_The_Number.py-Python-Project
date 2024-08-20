import random
Starting_value=1
Ending_value=10
randomnumber=random.randint(Starting_value,Ending_value)
print("Game Condition's: ")
print('1.You are give 4 Chances ')
print('You have to Guess the Number Correct')
print(' ')
l=4
for i in range(4):
    l-=1
    
    def rollo(): 
        while True:
            guess=input('Enter Your Guess Number form (1-10): ')
            if guess.isdigit():
                guess=int(guess)
                if 1<=guess<=10:
                    break
                else:
                    print('Enter Your Guess in Between the Numbers(1-10)')
            else:
                print('Invalid Input')
        return guess
    k=rollo()
    if k==randomnumber:
        print('Congratulation You Guessed It Right')
        break
    elif k!=randomnumber:
        print('You Guessed it Wrong',)
        print('Your Have ',l,'Chances Left')
    if l==0:
        print('The Actual Guess was : ',randomnumber)
        print('Better luck Next time ')




