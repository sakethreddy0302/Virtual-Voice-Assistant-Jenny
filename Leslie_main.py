import os
import pyttsx3
import speech_recognition
import pyautogui
import openai

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

#chat
chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "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"
    chatStr += f"User: {query}\n Jenny: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

#ai
def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,6)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hello" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello, How are you?")

                elif "i am fine" in query:
                    speak("That's great")

                elif "thank you" in query:
                    speak("You are welcome")

                elif "what is your name" in query:
                    speak("My name is Jenny")

                elif "jenny" in query:
                    speak("Yes, how can I help you")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                # youtube automation
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()

                # open and close of apps
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jenny","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")   

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query) 
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                # using ai to genarate
                elif "Using artificial intelligence".lower() in query.lower():
                    ai(prompt=query)
                    speak("Done")

                else:
                    print("Chatting...")
                    chat(query)
                