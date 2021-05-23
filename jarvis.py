import speech_recognition as sr
import webbrowser
from urllib import parse, request
import re
import win32com.client as wincl
import keyboard

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()

while True:
    try:
        if keyboard.is_pressed('º'):
            with sr.Microphone() as source:
                vocal_gen = "Diga el comando deseado"
                print(vocal_gen)
                speak.Speak(vocal_gen)
                audio = r.listen(source)

                try:
                    recognised_text = r.recognize_google(audio)
                    print(recognised_text)
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print("")

            if "musica" in recognised_text:
                recognised_text.replace("musica", "")
                busqueda = recognised_text
                query_string = parse.urlencode({'search_query': recognised_text})
                html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
                search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
                print(search_results)
                print(busqueda)
                speak.Speak("Buscando" + recognised_text + "en youtube")
                url = ('https://www.youtube.com/watch?v=' + search_results[0])
                try:
                    webbrowser.open_new_tab(url)
                except webbrowser.Error:
                    print("No se ha encontrado Chrome")
                    break

    except:
        print("")