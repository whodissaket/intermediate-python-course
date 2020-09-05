import random
def main():
    dice_rolls=int(input('How many die/dice would you like to roll ?? '))
    dice_size = int(input('How many sides are the dice? '))
    dice_sum=0
    for i in range(0 , dice_rolls):
        roll=random.randint(1,dice_size)
        dice_sum+=roll
        if roll == 1:
            print(f'You rolled a {roll}! Ooofffff !! :(')
        elif roll == 6:
            print(f'You rolled a {roll}! Lucky!! :) ')
        else:
            print(f'You rolled a {roll}')

    print(f'You have rolled a total of {dice_sum}')



if __name__== "__main__":
  main()
