# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
#
# l = ["Pranav", "Virat", "Rohit"]
# Your program should pronouce:
#
# Shoutout to Pranav
# Shoutout to Virat
# Shoutout to Rohit


# import speak as speak
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Pranav", "Virat", "Rohit"]

# speaker.Voice = speak.GetVoices().Item(2)
# speaker.Rate = 3
# print(speak.GetVoices().Item(2).GetDescription())  # just to see what voice is used

for word in l:
    speaker.Speak(f"Shoutout to {word}")
