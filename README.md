"VOICE ASSISTANT PROJECT USING PYTHON"

-->PROJECT DESCRIPTION
This project is a Python-based Voice Assistant that listens to user voice commands, converts speech into text, and responds using text-to-speech. It can perform basic tasks such as greeting the user, telling the current time and date, and opening websites like Google and YouTube.

-->PROJECT DESCRIPTION
.To learn speech recognition in Python
.To understand text-to-speech conversion
.To build a basic voice-controlled assistant
.To execute system and web-based commands using voice input
-->TECHNOLOGIES USED

.Python 3
.SpeechRecognition library
.PyAudio library
.pyttsx3 library
.datetime module
.webbrowser module

 -->SYSTEM REQUIREMENTS
.Python version 3.x
.Microphone (built-in or external)
.Internet connection for speech recognition
.Windows operating system

-->INSTALLATION STEPS
.Download or clone the project
.Open the project folder in VS Code
.Open the terminal in VS Code
.Install the required libraries using the command below

pip install SpeechRecognition pyttsx3 pyaudio

-->NOTE  
If PyAudio installation fails, download the suitable wheel file from  
https://www.lfd.uci.edu/~gohlke/pythonlibs/  
and install it using

pip install PyAudio-version.whl

--> HOW TO RUN THE PROJECT
.Open VS code
.Open the project folder
.Open terminal
.Run the following command

python voice_assistant.py

.Speak commands after the assistant greets you

-->SUPPORTED VOICE COMMANDS
.hello  
.time  
.date  
.open google  
.open youtube  
.exit or quit  
-->SAMPLE OUTPUT
Listening...
Recognizing...
User said: hello
Listening...
Recognizing...
User said:exit

--> AUTHOR
NARABOINA MANOJ KUMAR


