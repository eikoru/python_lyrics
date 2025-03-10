import time
from threading import Lock
import sys

lock = Lock()

def animate_text(text, delay=0.2):
    with lock:  
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def slang_song():
    lyrics = [
        ("Babalik ka ba?", 0.0, 0.2),
        ("Sa himbing ng pag-idlip ", 0.3, 0.3), 
        ("Tako'y ginising ng paglisan mo", 0.2, 0.2),
        ("Babalik ka bang muli", 0.2, 0.3),
        ("kahit na sa panaginip na lang?", 0.3, 0.3), 
    ]

    for lyric, delay, speed in lyrics:
        sing_lyric(lyric, delay, speed)

slang_song()