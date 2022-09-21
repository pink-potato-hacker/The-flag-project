from pygame import mixer

"""
This function will play ok i pull up while playing.
"""


def background_music():
    mixer.init()
    mixer.music.load('Music File/ok i pull up.mp3')
    mixer.music.play()


"""
This function will make a fart sound when player steps on mine - Lose.
"""


def bomb_sound():
    mixer.init()
    mixer.music.stop()
    bomb_sound = mixer.Sound("Music File/Bruh sound effect.mp3")
    mixer.Sound.play(bomb_sound)


"""
This function will make a bruh sound when player gets to the flag - Win.
"""


def victory_sound():
    mixer.init()
    mixer.music.stop()
    victory_sound = mixer.Sound("Music File/Bruh sound effect.mp3")
    mixer.Sound.play(victory_sound)