import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Simple Music Player")

music_folder = "Shugy.py/lab.7/music/musics"
songs = []

for file in os.listdir(music_folder):
    if file.endswith(".mp3"):
        songs.append(music_folder + "/" + file)

if len(songs) == 0:
    print("No songs found in the 'musics' folder.")
    sys.exit()

i = 0
paused = False

def play():
    global paused
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play()
    paused = False
    print("▶️ Now playing:", songs[i])

print("Controls: SPACE - play/pause | S - stop | N - next | P - previous | ESC - exit")

play()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("▶️ Resumed")
                else:
                    pygame.mixer.music.pause()
                    paused = True
                    print("⏸ Paused")

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("⏹ Stopped")

            elif event.key == pygame.K_n:
                i = (i + 1) % len(songs)
                play()

            elif event.key == pygame.K_p:
                i = (i - 1) % len(songs)
                play()

    pygame.display.flip()
    clock.tick(30)