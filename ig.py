from time import sleep

file_path = "/Users/johanchapelain/Documents/Dev/gfxhat_radio/followerNum.txt"

with open(file_path) as f:
    first_line = f.readline()

print(first_line)


while True:
    with open(file_path, "r") as f1:
        last_line = f1.readlines()[-1]
        print(last_line)
    sleep(10)

