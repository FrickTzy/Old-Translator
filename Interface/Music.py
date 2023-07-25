import random
import pygame

Music = ["Black Catcher.mp3", "Departure.mp3", "Chainsaw Man.mp3", "Dr. Stone.mp3", "Evangelion.mp3", "Horimiya.mp3",
         "Into the Night.mp3", "Justadice.mp3", "Tokyo Revengers.mp3", "Cupid.mp3", "Idol.mp3", "New Genesis.mp3",
         "Alive.mp3", "Night Dancer.mp3", "Overdose.mp3", "Wano Theme.mp3", "Hell's Paradise.mp3", "Unravel.mp3",
         "Noragami.mp3", "Sao.mp3", "Wotakoi.mp3", "Naruto.mp3", "Gurenge.mp3", "Jujutsu Kaisen.mp3",
         "Lost In Paradise.mp3", "Vivid Vice.mp3", "My War.mp3"]
x = 0
play = True
song_name = ""
switch = ""

random.shuffle(Music)


def music(window):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(Music[x])
    pygame.mixer.music.play(0)
    set_song_title()
    que(window)


def que(window):
    global x, Music, switch
    pos = pygame.mixer.music.get_pos()
    if int(pos) == -1:
        if x == (len(Music) - 1):
            x = -1
        x += 1
        switch += " "
        pygame.mixer.music.load(Music[x])
        pygame.mixer.music.play(0)
        set_song_title()

    window.after(1, lambda: que(window))


def change_music(window, direction: bool):
    global x, play
    if direction:
        if x == (len(Music) - 1):
            x = -1
        x += 1
    else:
        if x == 0:
            x = (len(Music))
        x -= 1
    play = True
    pygame.mixer.music.load(Music[x])
    pygame.mixer.music.play(0)
    set_song_title()

    window.after(1, lambda: que(window))


def change_volume(volume):
    pygame.mixer.music.set_volume(volume)


def play_music():
    global play
    if play:
        pygame.mixer.music.pause()
        play = False
    else:
        pygame.mixer.music.unpause()
        play = True


def set_song_title():
    global x, Music, song_name
    return Music[x].removesuffix(".mp3")
