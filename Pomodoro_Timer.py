"""
Pomodoro Timer CLI with cross-platform sound notifications.
"""

import time
import pygame

def beep():
    """Plays a short beep sound at the start or end of a session."""
    try:
        pygame.mixer.init()
        sound = pygame.mixer.Sound("Pomodoro-Timer-in-Python-CLI-/beep.wav")
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))
    except pygame.error as e:
        print(f"(Beep skipped: {e})")

def countdown(mins, label):
    """Handles the countdown for both work and break sessions"""
    print(f"\n{label.upper()} TIME STARTS.\n")
    time.sleep(1)
    seconds = 0
    # Display timer in MM:SS format
    while True:
        print(f" {mins:02d}:{seconds:02d}", end = "\r", flush = True)
        if seconds != 0:
            seconds -= 1
        elif mins != 0:
            mins -= 1
            seconds = 59
        else:
            # Play a sound when the timer ends
            beep()
            print(f" 00:00\n{label.upper()} TIME OVER.\n")
            break
        time.sleep(1)

def transition(next_label):
    """Add a 5-second delay between work and break sessions"""
    print(f"{next_label.upper()} TIME STARTS IN 5 SECONDS")
    for i in range(5, 0, -1):
        print(f" 00:0{i}", end = "\r", flush = True)
        time.sleep(1)       

def main():
    """Control flow of the Pomodoro Timer"""
    print("\n------- POMODORO TIMER -------\n")
    try:
        work_mins = int(input("Enter work minutes: "))
        break_mins = int(input("Enter break minutes: "))
        rounds = int(input("Enter number of rounds: "))
        copy = rounds

        while rounds != 0:
            countdown(work_mins, "work")
            transition("break")
            countdown(break_mins, "break")
            if rounds == 1:
                break
            transition("work")
            rounds -=1

        # Display the final stats
        print(
            f"Total Productive Time: {copy*work_mins} minutes, "
            f"Total Break Time: {copy*break_mins} minutes, "
            f"Rounds: {copy}"
            )
        beep()
        print("Pomodoro Ended!\n----------------------------")
    except ValueError:
        print("Invalid Input. Please enter numeric values.")

if __name__ == "__main__":
    main()

# End of Code.
