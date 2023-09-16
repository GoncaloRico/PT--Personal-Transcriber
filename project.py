import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time
import sys

def main(): #This function will record an audio as soon as the program runs, until a key is pressed, interrupting the recording, and then play it back to the user.
    duration = collect_user_input()
    save_or_not, SAMPLE_RATE, audio_recording = record(duration)
    voice_file_name = save_recording(save_or_not)
    text_file_name = voice_file_name.replace(".wav", ".txt")
    text_from_voice = recording_to_text(voice_file_name)
    save_text_file(text_from_voice, text_file_name)


def collect_user_input():
    while not isinstance(user_input, int): #This will loop the request for user input on the amount of seconds the recording should be, until an integer is submitted
        try:
            user_input = int(input("How long do you want this recording to be? (Please insert duration in seconds) "))
        except ValueError:
            print("Please insert an Integer.")
    return(user_input)


def record(duration):
    SAMPLE_RATE = 48000
    audio_recording = sd.rec(duration * SAMPLE_RATE, samplerate = SAMPLE_RATE, channels = 2, dtype = "int32")
    print("Recording Audio")
    sd.wait()
    print("Audio Recording complete, Playing Audio")
    sd.play(audio_recording, SAMPLE_RATE)
    sd.wait()
    while True:
        save = (input("Playback finished, do you want to save this recording? Please select yes or no. ") ).lower()
        if save in ["yes", "y", "no", "n"]:
            return save, SAMPLE_RATE, audio_recording
        else:
            print("Invalid input, please try again")


def save_recording(save_or_not, SAMPLE_RATE, audio_recording): #This processes whether the voice file will be saved or discarded
    if save_or_not in ["yes", "y"]:
        voice_file_name = time.strftime("%d_%m_%Y-%H_%M_%S.wav")
        wav.write(voice_file_name, SAMPLE_RATE, audio_recording)
        return(voice_file_name)
    else:
        sys.exit("Recording will not be saved")


def recording_to_text(voice_file_name):
    r = sr.Recognizer()
    with sr.AudioFile(voice_file_name) as source: #This will open the file
        audio_data = r.record(source) #load audio to memory
        text = r.recognize_google(audio_data) #convert from speech to text
        return text


def save_text_file(text_from_voice, text_file_name):
    with open(text_file_name, "w") as f:
        f.write(text_from_voice)
    print("Your Audio Recording has been turned to text.")

if __name__ == "__main__":
    main()
