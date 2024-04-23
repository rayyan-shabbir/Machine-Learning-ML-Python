import speech_recognition as sr
import moviepy.editor as mp
import re

# Load the video file and extract its audio
clip = mp.VideoFileClip(r"motivation.mp4")
clip.audio.write_audiofile(r"converted_mp3.wav")

# Initialize the speech recognizer
r = sr.Recognizer()
audio = sr.AudioFile(r"converted_mp3.wav")

# Open the audio file and record its content
with audio as source:
    audio_file = r.record(source)

# Recognize speech and store the result
result = r.recognize_google(audio_file)

# Split the recognized text into individual words
words = re.findall(r'\b\w+\b', result.lower())

# Store words and their timestamps
word_timestamps = {}
for i, word in enumerate(words):
    word_timestamps.setdefault(word, []).append(i)

# Write the recognized speech and timestamps to a file
with open('recog.txt', mode='w') as file:
    file.write("Speech Recognized\n")
    file.write(result)
    file.write("\n\nWord Timestamps:\n")
    for word, timestamps in word_timestamps.items():
        file.write(f"{word}: {timestamps}\n")

print("File is ready.....")

# Prompt the user to search for a word
search_word = input("Enter a word to search: ").lower()
# Check if the word exists in the timestamps
if search_word in word_timestamps:
    print(f"'{search_word}' found at timestamps: {word_timestamps[search_word]}")
else:
    print(f"'{search_word}' not found.")
print("Enter exist to exit from program......!")    


