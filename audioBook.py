import pyttsx3
import speech_recognition as sr
import PyPDF2

speaker = pyttsx3.init()
listener = sr.Recognizer()


# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('Listening....')
#             voice = listener.listen(source)
#             co = listener.recognize_google(voice)
#             co = co.lower()
#     except:
#         pass
#     return co


# def c():
#     speaker.say('which page should i read')
#     speaker.runAndWait()
#     p = take_command()
#     print(p)
#     book = open('C.pdf', 'rb')
#     PdfReader = PyPDF2.PdfFileReader(book)
#     pages = PdfReader.numPages
#     print(pages)
#     page = PdfReader.getPage(p-1)
#     text = page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()


def readbook():
    speaker.say('which book should i read')
    speaker.runAndWait()
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            co = listener.recognize_google(voice)
            co = co.lower()
            print(co)
            if 'c programming' in co:
                speaker.say('which page should i read')
                speaker.runAndWait()
                try:
                    with sr.Microphone() as source:
                        print('Listening....')
                        voice = listener.listen(source)
                        p = listener.recognize_google(voice)
                        p = p.lower()
                        print(p)
                        book = open(
                            'C:/Python-project/Alexa/Unit 1-converted (1).pdf', 'rb')
                        PdfReader = PyPDF2.PdfFileReader(book)
                        # pages = PdfReader.numPages
                        # print(pages)
                        page = PdfReader.getPage(p)
                        text = page.extractText()
                        speaker.say(text)
                        speaker.runAndWait()
                except:
                    pass
    except:
        pass
