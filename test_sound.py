import pygame
import time

pygame.mixer.init()
beep = pygame.mixer.Sound("Pomodoro-Timer-in-Python-CLI-/beep.wav")
beep.play()
pygame.time.wait(int(beep.get_length() * 1000))
print("Beep finished.")
