from pygame import mixer

def background_music():
    mixer.init()
    mixer.music.load('Music File/Popcorn Original Song.mp3')
    mixer.music.play()

