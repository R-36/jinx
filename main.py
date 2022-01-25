import pyttsx3
import speech_recognition
import weather
from oxxxy import oxxxy
from obscene_antifilter import obscene_adder
from music_player import MusicPlayer


class Jinx(object):
    def __init__(self):
        self.voice_engine = pyttsx3.init()  # Система синтеза речи.
        self.listen_engine = speech_recognition.Recognizer()
        self.ru_voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\TokenEnums\\RHVoice\\Artemiy'

    def listen(self):
        """ Метод speech to text.

        Returns:
            query (str): Распознанная речь.
        """
        with speech_recognition.Microphone() as mic:
            self.listen_engine.adjust_for_ambient_noise(source=mic, duration=0.1)
            audio = self.listen_engine.listen(source=mic)
            query = obscene_adder(self.listen_engine.recognize_google(audio_data=audio, language='ru-RU').lower())
            with open("your_speech.wav", "wb") as file:
                file.write(audio.get_wav_data())
            return query

    def say(self, words, speed=150):
        """ Метод text to speech.

        Args:
            words (str): Текст, который нужно озвучить.
            speed (str): Скорость произнесения текста.
        """
        self.voice_engine.setProperty('voice', self.ru_voice_id)
        self.voice_engine.setProperty('rate', speed)
        self.voice_engine.say(words)
        self.voice_engine.runAndWait()

    def get_weather(self, place):
        print(weather.get_weather(place))
        self.say(weather.get_weather(place))

    def news(self):
        self.say('Главная новость текущей недели заключается в том, что я пукнул')

    def can(self):
        text = self.listen()
        print(text)
        if text[0] == 'погода':
            print(text)
            self.get_weather(text[1])
        elif text[0] == 'раунд':
            oxxxy(self)
        elif text[0] == 'включи' and text[1] == 'музыку':
            player = MusicPlayer()
            player.play()
        elif text[0] == 'новости':
            self.news()



nn = Jinx()
nn.can()
