import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio as pa
import wikipedia
import smtplib
engine= pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)    

def date():
    year =int(datetime.datetime.now().year)    
    month =int(datetime.datetime.now().month)  
    date =int(datetime.datetime.now().day)  
    speak("the current date is")  
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!") 
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour>18 and hour<24:
        speak("good evening sir!")
    else:
        speak ("Good night sir!")        
          
    speak(" Jarvis at your service. Please tell me how can i help you?")


def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source) 
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio ,language='en-in')     
        print(query)

    except Exception as e:
        print(e)  
        speak("Parden please...")  
        return "None"
    return query    

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.echlo()
    server.starttls()
    server.login('vaishalid4004@gmail.com',123)
    server.sendmail('vaishalid4004@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()    
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result =wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)   
        # elif'send email' in query:
        #     try:
        #         speak("What should I say?")
        #         content=takeCommand()
        #         to='vaishalibhor34@gmail.com'
        #         sendEmail(to,content)
        #         speak("Email has sent successfully!")
        #     except Exception as e:
        #         print(e)
        #         speak("Unable to send the email")

        elif 'offline' in query:
            quit()    