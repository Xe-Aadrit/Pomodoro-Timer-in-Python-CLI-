import time
import winsound

def countdown(mins, label):
    print(f"\n{label.upper()} TIME STARTS.\n")
    time.sleep(1)
    w_s = 0
    
    while True:
        print(f"{mins:02d}:{w_s:02d}", end = "\r", flush = True)
        if w_s != 0:
            w_s -= 1
        elif mins != 0:
            mins -= 1
            w_s = 59
        else:
            winsound.Beep(700, 350)
            print(f"00:00\n{label.upper()} TIME OVER.\n")
            break
        time.sleep(1)

def transition(next_label):
    print(f"{next_label.upper()} TIME STARTS IN 5 SECONDS")
    for i in range(5, 0, -1):
        print(f"00:0{i}", end = "\r", flush = True)
        time.sleep(1)       

def main():
    print("\n======= POMODORO TIMER =======\n")
    try:
        work_mins = int(input("Enter work minutes:"))
        break_mins = int(input("Enter break minutes:"))
        rounds = int(input("Enter number of rounds:"))
        copy = rounds

        while rounds != 0:
            countdown(work_mins, "work")
            transition("break")
            countdown(break_mins, "break")
            if rounds == 1:
                break
            transition("work")
            rounds -=1

        print(f"Total Productive Time: {copy*work_mins} minutes, Total Break Time: {copy*break_mins} minutes, Rounds: {copy}")
        winsound.Beep(1000, 1000)
        print("Pomodoro Ended.\n==============================")
    except ValueError:
        print("Invalid Input.")

main()