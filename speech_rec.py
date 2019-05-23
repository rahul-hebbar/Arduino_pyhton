import pyttsx3
import speech_recognition as sr
import serial

engine = pyttsx3.init('sapi5')
ser = serial.Serial('COM7', 9600)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


speak('Hello Sir, I am your digital assistant JARVIS!')
speak('How may I help you?')


def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':
    flag = True
    while flag:

        query = mycommand()
        query = query.lower()

        if 'turn on the led' in query:
            speak('led on')
            d = '1'
            ser.write(d.encode())

        elif 'turn off the led' in query:
            speak('led of')
            q = '0'
            ser.write(q.encode())

        elif 'bye' in query:
            speak('bye')
            flag = False;
            break

        speak('Next Command! Sir!')

