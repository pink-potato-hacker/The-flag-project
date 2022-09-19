from pygame import mixer

"""
This function will play background music while playing.
"""


def background_music():
    mixer.init()
    mixer.music.load('Music File/Popcorn Original Song.mp3')
    mixer.music.play()


"""
This function will make a "boom" sound when player steps on mine - Lose.
"""


def bomb_sound():
    mixer.init()
    mixer.music.stop()
    bomb_sound = mixer.Sound("Music File/Explosion sound effect.wav")
    mixer.Sound.play(bomb_sound)


"""
This function will make a winning sound when player gets to the flag - Win.
"""


def victory_sound():
    mixer.init()
    mixer.music.stop()
    victory_sound = mixer.Sound("Music File/Victory Sound Effect.wav")
    mixer.Sound.play(victory_sound)