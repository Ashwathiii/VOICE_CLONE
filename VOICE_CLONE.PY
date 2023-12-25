# importing library for video editing and audio extraction
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import moviepy.editor as mp
#input the video file
videofile=r"C:\Users\aswat\Desktop\DL PROJECTS\VOICE_CLONE_ASSIGNMENT\taylorswift.mp4"
output_audio="extracted_audio.wav"  #to save as extracted audio
#extracting audio from video
ffmpeg_extract_audio(videofile,output_audio)
#using audiofileclip to load the audio ,so that we can perform various operations on it
audio=mp.AudioFileClip(output_audio)

#converting the audio to text
#importing speech rec library
import speech_recognition as sr
recognizer=sr.Recognizer()
audio_file="extracted_audio.wav"
source_lang="en"  #replace it according to the language
#loading the audio
audio=sr.AudioFile(audio_file)
#converting the audio to text(google web speech api)
try:
    with audio as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language=source_lang)
        print("Recognized text in the source language:")
        print(text)

        # Save the recognized text to a text file
        with open("audio_text.txt", "w", encoding="utf-8") as text_file:
            text_file.write(text)

        print("Recognized text saved to audio_text.txt")

except sr.UnknownValueError:
    print("Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")


#Translation
#importing library for language translation and text to speech
from googletrans import Translator
from gtts import gTTS

# Read the saved text file
with open("audio_text.txt", "r", encoding="utf-8") as text_file:
    eng_text = text_file.read()

# Translate the text to desired lang using google web speech api
translator=Translator()
translation = translator.translate(eng_text, src="en", dest="hi")
hindi_text = translation.text

# Convert the text to speech using gTTS
tts = gTTS(text=hindi_text, lang='hi')
tts.save("translated_to_hindi.mp3")
print("saved as translated_to_hindi.mp3")


#converted audio is translated to speakers voice using RVC v2 with crepe
link="https://colab.research.google.com/drive/1Gj6UTf2gicndUW_tVheVhTXIIYpFTYc7?usp=sharing#scrollTo=OVQoLQJXS7WX"

#combining thevideo and the audio
#orginal video importing
video=mp.VideoFileClip(r"C:\Users\aswat\Desktop\DL PROJECTS\VOICE_CLONE_ASSIGNMENT\taylorswift.mp4")
#translated audio importing
audio=mp.AudioFileClip(r"C:\Users\aswat\Desktop\DL PROJECTS\VOICE_CLONE_ASSIGNMENT\audiotaylorswift_trans.wav")

#putting audio into this vdo
video=video.set_audio(audio)

#resizing
video = video.resize(width=1000, height=700)

#saving
video.write_videofile("final_output.mp4")
print("video saved as final_output.mp4")

#loading the video with the audio
final_video="final_output.mp4"  #actually give the path here

videoclip=mp.VideoFileClip(final_video)
videoclip.preview()
videoclip.close()
