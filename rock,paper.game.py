import random
print('hello welcome to this game .')
a='yes'
b=0
computer=0
user=0
while a =='yes':
    item=['paper','rock','scissors']
    computer_choice=random.choice(item)
    user_choice=input('please select your item: (paper , rock , scissors) ')
    print(f'computer choice :  {computer_choice}')
    if user_choice==computer_choice:
        print(f'tie ')
        print('-'*20)
        user=user+1
        computer=computer+1
    elif user_choice=='paper':
        if computer_choice=='scissors':
            print(f'computer win')
            print('-'*20)
            computer=computer+1
        else:
            print('you win')
            print('-'*20)
            user=user+1
    elif user_choice=='rock':
        if computer_choice=='paper':
            print('computer win')
            print('-'*20)
            computer=computer+1
        else:
            print('you win')
            print('-'*20)
            user=user+1
    elif user_choice=='scissors':
        if computer_choice=='rock':
            print('computer win')
            print('-'*20)
            computer=computer+1
        else:
            print('you win')
            print('-'*20)
            user=user+1
    else:
        print('sorry eror ')
        exit()
    b=b+1
    print(f'number you played : {b}')
    print('-'*20)
    print(f'computer score : {computer}')
    print(f'your score : {user}')
    a=input('do you want to play again? ')
if a =='no':
    print('thank you to visit')
