# 

#playing audio from sd card
import board, time, neopixel, pwmio
import os, ssl, socketpool, wifi, mount_sd
import busio,  storage, sdcardio

# Statements Touchpad
import adafruit_mpr121
import digitalio
i2c = board.STEMMA_I2C()
touch_pad = adafruit_mpr121.MPR121(i2c)
#lights 
import neopixel
strip = neopixel.NeoPixel(board.GP28, 30)
#audio
from audiopwmio import PWMAudioOut as AudioOut
from audiomp3 import MP3Decoder
from audiocore import WaveFile
path = "/sd/wb/"

# Setup speaker
audio = AudioOut(board.GP16) # assuming tip of Audio pin to GP16


# Setup MP3 decoder
filename = "theme.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)


#names of sound files
wb =["bugsbunny",
"Harry",
"history",
"Inception",
"Scoopy",
"theme"]
#function to play sounds
def play_sound1(filename, pad_number):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            if not touch_pad[pad_number].value: # if no longer being touched
                audio.stop()




from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile
def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass
            
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)
#mp3s
def play_mp3(filename):
    decoder.file = open(path + filename, "rb")
    audio.play(decoder)
    while audio.playing:
        if touch_pad[6].value:
            audio.stop()
            

BLUE = (0, 0, 255)


playing = False  # keep track of whether a sound is currently playing
current_file = None  # keep track of the file being played (if any)

stop_touch_pad = 6  # the touch pad number to stop the sound

while True:
    for i in range(len(wb)):
        if touch_pad[i].value:
            #play_sound(wb[i], i)
            strip.fill(BLUE)
            filename = f"{i}.mp3"
            #play_sound(filename)
            #filename = f"{i}.mp3"
            #print(f"playing : {filename}")
            play_mp3(filename)
            strip.fill((0,0,0))
