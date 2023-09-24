import pygame
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound
swing_sound = pygame.mixer.Sound('swing_sound.wav')
hit_sound = pygame.mixer.Sound('hit_sound.wav')

# Set volume (optional)
swing_sound.set_volume(1)
hit_sound.set_volume(1)

# Play swing sound
print("Playing swing sound...")
swing_sound.play()

# Wait a few seconds
time.sleep(2)

# Play hit sound
print("Playing hit sound...")
hit_sound.play()

# Wait a few seconds to let the sound play
time.sleep(2)
