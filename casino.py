import random as r
import time as t
punkte = 5
print("Vítej v casinu")
while True:
    try:
        range = int(input("Jakou chceš mít horní hranici pro náhodné číslo? Čím vyšší rozdíl, tím vyšší odměna: "))
        guess = int(input(f"Typni si číslo od 1 do {range}: "))
        number = r.randint(1, range)
        reward = range-1

        if guess == number:
            print(f"Gratulujeme, vyhrál jsi {reward} magických bodíků")
            punkte += reward
        else:
            print(f"Bohužel jsi prohrál/a, počítač vybral číslo {number}")
            punkte -= 1
        print("Máš", punkte, "bodíků")
        if punkte <= 0:
            print("Došly ti peníze, bohužel končíš")
            t.sleep(1.5)
            break
    except ValueError:
        print("Zadaná hodnota není číselná")
        continue

