import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("hii, i am anniy . Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:
       
        print("Say that again please...")
        command = takeCommand();
        
    return command

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        command = takeCommand().lower()

        
        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif'open reddit' in command:
            speak("opening reddit....")
            webbrowser.open("reddit.com")

        elif 'open youtube' in command:
            speak("opening youtube....")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")
            
        elif 'joke' in command:
            webbrowser.open("icanhazdadjoke.com")
            speak()

        elif 'open stack overflow' in command:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in command:
            music_dir = 'F:\jb'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in command:
            codePath = "D:\ankassist.py\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in command:
           speak('Who is the recipient?')
           recipient = takeCommand()
           if 'swati' in recipient:
            speak('What should I say?')
            content = takeCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('akr19547@gmail.com', '7277780075')

            #send message
            mail.sendmail('swati', 'swati.patel.1697@gmail.com', content)

            #end mail connection
            mail.close()
            speak("Email has been sent!")
           else: 
            speak("Sorry my friend Ankit. I am not able to send this email")
            
speak('I am ready for your command')
        
while True:
    wishMe(takeCommand())