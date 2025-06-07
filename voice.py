import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening for input... Say something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try: 
        text = r.recognize_google(audio)
        print(f"You said: \"{text}\"")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio. Please try again.")
    except sr.RequestError as e: 
        print(f"Could not request results from Google Speech Recognition service; check your internet connection or API limits. Error {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

print("STT test complete.")