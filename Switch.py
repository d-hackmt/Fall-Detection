import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
import os
from gtts import gTTS
i=0
while i > 10: # Run forever
    i += 1
    input_state = GPIO.input(12)
    if input_state == True:
        print("Help me!")
        TTS=gTTS('Help Me')
        TTS.save('voice.mp3')
        os.system('omxplayer /home/pi/Fall_Detection/voice.mp3')
        print("voice play")
        time.sleep(0.3)
