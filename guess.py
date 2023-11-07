word ="USMAN".lower()
guess =""
counts = 0
tries = 5
out_of_tries = False

while guess != word and not (out_of_tries):
    if counts < tries:
        guess = input("ENTER YOUR GUESS: ").lower()
        counts += 1
    else:
        out_of_tries = True

if out_of_tries:
    print("YOU LOSE!\n TRY AGAIN")
else:
    print("YOU WIN")

