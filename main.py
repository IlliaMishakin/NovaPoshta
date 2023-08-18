import subprocess
import speech_recognition as sr
from gtts import gTTS


class ParcelInfoAsker:

    SENDER_QUESTIONS = ["Прізвище, ім'я, по-батькові.",
                        "Адреса відправника.",
                        "Мобільний телефон відправника.",
                        "Місто доставки відправлення."]

    RECIPIENT_QUESTIONS = ["Прізвище, ім'я, по-батькові.",
                           "Адреса отримувача.",
                           "Мобільний телефон отримувача.",
                           "Місто доставки відправлення."]

    GENERAL_QUESTIONS = ["Назвіть вартість відправлення.",
                         "Назвіть платника послуг (відправник чи одержувач)."]

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.sender_info = {}
        self.recipient_info = {}
        self.general_info = {}

    def ask_question(self, question):
        tts = gTTS(question, lang='uk')
        tts.save("question.mp3")
        subprocess.call([r"C:\OGIlya\ffmpeg-6.0-essentials_build\bin\ffplay.exe", "-nodisp", "-autoexit",
                         "question.mp3"])

    def record_response(self):
        with sr.Microphone() as source:
            print('speak!')
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)

            return self.recognizer.recognize_google(audio, language="uk-UA")

    def build_dialogue(self):
        self.ask_question("Надайте, будь-ласка, наступні дані отримувача: ")
        for sender_question in self.SENDER_QUESTIONS:
            self.ask_question(sender_question)
            print("Assistant: ", sender_question)
            response = self.record_response()
            print("User: ", response)

        for recipient_question in self.RECIPIENT_QUESTIONS:
            self.ask_question(recipient_question)
            print("Assistant: ", recipient_question)
            response = self.record_response()
            print("User: ", response)

        for general_question in self.GENERAL_QUESTIONS:
            self.ask_question(general_question)
            print("Assistant: ", general_question)
            response = self.record_response()
            print("User: ", response)



def main():
    question_recorder = ParcelInfoAsker()
    question_recorder.build_dialogue()

if __name__ == "__main__":
    main()





