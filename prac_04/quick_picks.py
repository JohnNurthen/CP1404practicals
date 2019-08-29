import random

MIN_NUMBER = 1
MAX_NUMBER = 45
TOTAL_NUMBERS_SELECTED = 6


def main():
    number_of_quick_picks = int(input('How many quick picks would you like?: '))

    for quick_picks in range(number_of_quick_picks):
        quick_pick = []
        for number in range(TOTAL_NUMBERS_SELECTED):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(' '.join('{:2}'.format(number) for number in quick_pick))


main()
