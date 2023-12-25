# VOICE CLONING
This project extracts audio from a video
Performs speech recognition,
Translates the speech to recognized text, 
Converts the text to speech,
Converts the speech to the speaker's voice using RVC v2 with Crepe, 
And creates a video with the converted speaker-modified audio.


- (Requirements)(#requirements)
- (Usage])(#usage)
  - [1. Audio Extraction](#1-audio-extraction)
  - [2. Speech Recognition](#2-speech-recognition)
  - [3. Translation](#3-translation)
  - [4. Text-to-Speech Conversion](#4-text-to-speech-conversion)
  - [5. Audio Conversion (RVC v2 with Crepe)](#link)
  - [6. Video Creation](#6-video-creation)


  ## Requirements

Ensure you have the following installed:

- Python 3.6 or higher installed
- Required Python libraries: moviepy, speech_recognition, googletrans==4.0.0, gtts
- FFmpeg (for audio extraction)

Install the required libraries using:

```bash
pip install moviepy SpeechRecognition googletrans==4.0.0 gtts


