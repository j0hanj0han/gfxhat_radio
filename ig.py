from time import sleep

file_path = "/Users/johanchapelain/Documents/Dev/gfxhat_radio/followerNum.txt"

def get_followers_from_file():
        with open(file_path, "r") as f1:
            last_line = f1.readlines()[-1]
            followers = str(last_line)
            return followers

print(get_followers_from_file())




