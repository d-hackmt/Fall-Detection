import time
import os
from gtts import gTTS
print("Welcome to Pill Reminder System For Elderly Peaple")

def pill_reminder():
    print("I reminder You in every 1 minutes...Stay Home!!Stay Safe!!")
    print('Morning Pill Reminder')
    local_time = 1.0 * 60
    time.sleep(local_time)
    TTS=gTTS('Morning Pill Reminder')
    TTS.save('voice.mp3')
    os.system('omxplayer /home/pi/voice.mp3')
    print('Afternoon Pill Reminder')
    local_time1 = 1.0  * 60
    time.sleep(local_time1)
    TTS=gTTS('Afternoon Pill Reminder')
    TTS.save('voice1.mp3')
    os.system('omxplayer /home/pi/voice1.mp3')
    print('Done')
    

if __name__== "__main__":
    pill_reminder()


