import pyttsx3
while True:
   text_speech = pyttsx3.init()

   answer = input("What you want to speak : ")
   if answer=="q":
       break
   text_speech.say(answer)
   text_speech.runAndWait()
