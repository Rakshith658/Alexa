import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def swm():
    engine.say('please say number')
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            print('Listening....')
            number = listener.listen(source)
            commandN = listener.recognize_google(number)
            print(commandN)
            engine.say('what is the message')
            engine.runAndWait()
            print('Listening....')
            message = listener.listen(source)
            commandM = listener.recognize_google(message)
            commandM = commandM.lower()
            print(commandM)
            # ch = datetime.datetime.now().strftime('%H')
            # cm = datetime.datetime.now().strftime('%M')
            now = datetime.datetime.now()
            m = now.minute + 1
            pywhatkit.sendwhatmsg(
                '+91'+commandN, commandM, now.hour, m)
    except:
        pass
