from pygame import mixer

def background_music():
    mixer.init()
    mixer.music.load('Music File/Popcorn Original Song.mp3')
    mixer.music.play()

def bomb_sound():
    mixer.music.stop()
    bomb_sound = mixer.Sound("Music File/Loud Explosion Sound Effect (HD) (3).mp3")
    mixer.Sound.play(bomb_sound)
