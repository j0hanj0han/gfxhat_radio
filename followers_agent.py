from time import sleep

from Display import Display
from ig import get_followers_from_file


def display_last_followers_informations():
    while True:
        followers = get_followers_from_file()
        display = Display(followers)
        display.show()
        print(followers)
        sleep(1)

display_last_followers_informations()


