from gtts import gTTS

# Текст, который нужно сгенерировать в аудио
text = "Hello, how are you?"

# Генерация аудио из текста
tts = gTTS(text)
print(type(tts))