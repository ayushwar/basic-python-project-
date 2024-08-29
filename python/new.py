import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen_and_convert():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                
                # Check for stop command
                if "stop" in text.lower():
                    engine.say("Stopping the program. Goodbye!")
                    engine.runAndWait()
                    break

                # Save the text to a file
                save_to_notepad(text)

                # Provide feedback
                engine.say("Saved to notepad.")
                engine.runAndWait()

            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                engine.say("Sorry, I did not understand that.")
                engine.runAndWait()
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service")
                engine.say("Could not request results from the Google Speech Recognition service.")
                engine.runAndWait()

def save_to_notepad(text):
    with open("output.txt", "a") as file:
        file.write(text + "\n")

if __name__ == "__main__":
    engine.say("The program is running. Say 'stop' to end.")
    engine.runAndWait()
    listen_and_convert()
