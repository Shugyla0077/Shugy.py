import pygame
pygame.init()

num_mus = 0
paused = True

prev_b = pygame.image.load("Shugy.py/lab.7/2music_player/images/previous.png")
play_b = pygame.image.load("Shugy.py/lab.7/2music_player/images/play.png")
next_b = pygame.image.load("Shugy.py/lab.7/2music_player/images/next.png")

music_list = [
    "Shugy.py/lab.7/2music_player/sounds/Dynamite.mp3",
    "Shugy.py/lab.7/2music_player/sounds/asylym.mp3",
    "Shugy.py/lab.7/2music_player/sounds/hikaya.mp3",
    "Shugy.py/lab.7/2music_player/sounds/poushi.mp3"
]

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Music player")

label = pygame.font.Font('Shugy.py/lab.7/2music_player/fonts/Roboto-Black.ttf', 30)

name_list = [
    label.render("Dynamite - BTS", True, (255,255,255)),
    label.render("Asylym - ASHA Prince", True, (255,255,255)),
    label.render("Hikaya - Madmen", True, (255,255,255)),
    label.render("По уши в тебя влюблен - Miyagi & Andy Panda", True, (255,255,255))
]

pygame.mixer.music.load(music_list[num_mus])
pygame.mixer.music.play()
pygame.mixer.music.pause()

running = True
while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 300, 700, 200))
    screen.blit(prev_b, (210, 370))
    screen.blit(play_b, (315, 370))
    screen.blit(next_b, (410, 370))
    screen.blit(name_list[num_mus], (30, 30))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            elif event.key == pygame.K_KP_ENTER:
                pygame.mixer.music.stop()
                paused = False

            elif event.key == pygame.K_RIGHT:
                num_mus += 1
                if num_mus >= len(music_list):
                    num_mus = 0
                pygame.mixer.music.load(music_list[num_mus])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                num_mus -= 1
                if num_mus < 0:
                    num_mus = len(music_list) - 1
                pygame.mixer.music.load(music_list[num_mus])
                pygame.mixer.music.play()
