name = input('Print your name: ')
print('Welcome', name, 'to your worst nightmare')

answer = input('You are on a dirt road. It has come to an end.  You can go left or right. Which way would you like to go? ').lower()
if answer == 'left':
    answer = input('You come to a river.  You can go around it or swim across it. Type walk to walk around it or swim to swim across: ')
    if answer == 'swim':
        print('You swam across and were devoured by piranhas.')
    elif answer == 'walk':
        print('You walked for many miles, but Paige is with you and she forgot her ipad and keeps plugging her ears.')
    else:
        print('You lose.  Good day!')


elif answer == 'right':
    answer = input('You come to a bridge.  It looks wobbly. Do you want to cross it or head back (cross/back)?')

    if answer == 'back':
        print('You go back to the main road.  And Jimmy Gilbert pooped out to be creepy. And now you are dead.')
    elif answer == 'cross':
        answer = input('You cross the bridge and meet up with Delaney Deevers.  Do you talk to them (ye/no)? ')

        if answer == 'yes':
            print('You talk to Delaney Deevers.  He says Doroodoo.  and he takes you to Laxmi Palace. You win!')

        elif answer == 'no':
            print('You ignore Delaney Deevers.  ')

        else:
            print('Not a valid answer.  You lose.  Good day.')

    else:
        print('You lose.  Good day!')
else:
    print('You lose.  Good day!')
print('Thank you for trying,' + name)
