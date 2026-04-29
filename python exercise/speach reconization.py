import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting noise...")
    recognizer.adjust_for_ambient_noise(source)

    print("Recording for 4 seconds...")
    audio = recognizer.listen(source, timeout=4)

    print("Recording complete.")

try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio, language="en-US")
    print("Recognized text:", text)

except Exception as e:
    print("Error:", e)