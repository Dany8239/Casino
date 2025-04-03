import random as r
import time as t
punkte = 5
consecutive_wins = 0
consecutive_losses = 0
print("Vítej v casinu")
def calculate_reward(consecutive_wins, consecutive_losses, range):
    basereward = range - 1
    if consecutive_wins > 3:
       reward = basereward - (consecutive_wins * 0.5)
    elif consecutive_losses > 3:
        reward = basereward + (consecutive_losses * 0.5)
    else:
        reward = basereward
    reward = round(reward)
    if reward < 1:
        reward = 1
    elif reward > 100:
        reward = 100
    return reward

while True:
    try:
        range = int(input("Jakou chceš mít horní hranici pro náhodné číslo? Čím vyšší rozdíl, tím vyšší odměna, minimum je 5: "))
        if range < 5:
            print("Hodnota musí být alespoň 5")
            continue
        reward = calculate_reward(consecutive_wins, consecutive_losses, range)
        confirm = input(f"Momentální odměna je: {reward} magických bodíků. Chceš pokračovat? (a/n): ").lower()
        if confirm != "a":
            continue
        guess = int(input(f"Typni si číslo od 1 do {range}: "))
        number = r.randint(1, range)
        t.sleep(0.5)
        if guess == number:
            print(f"Gratulujeme, vyhrál jsi {reward} magických bodíků")
            punkte += reward
            consecutive_wins += 1
            consecutive_losses = 0
        else:
            print(f"Bohužel jsi prohrál/a, počítač vybral číslo {number}")
            punkte -= 1
            consecutive_losses += 1
            consecutive_wins = 0
        print("Máš", punkte, "bodíků")
        if punkte <= 0:
            print("Došly ti peníze, bohužel končíš")
            t.sleep(1.5)
            break
    except ValueError:
        print("\nZadaná hodnota není číselná")
        continue
    except KeyboardInterrupt:
        print("\nUkončuji program, měl jsi", punkte, "bodíků")
        t.sleep(1.5)
        break
    except Exception as e:
        print(f"\nNastala neočekávaná chyba: {e}")
        t.sleep(1.5)
        break

