from pygame import mixer

def background_music():
    mixer.init()
    mixer.music.load('Music File/Popcorn Original Song.mp3')
    mixer.music.play()


def bomb_sound():
    mixer.init()
    mixer.music.stop()
    bomb_sound = mixer.Sound("Music File/Explosion sound effect.wav")
    mixer.Sound.play(bomb_sound)


def victory_soud():
    mixer.init()
    mixer.music.stop()
    victory_sound = mixer.Sound("Music File/Victory Sound Effect.wav")
    mixer.Sound.play(victory_sound)