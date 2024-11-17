from gtts import gTTS

# Convert text to speech
def text_to_speech( text, file_name):
  mapper = { 'hin_Deva': 'hi' }
  tts = gTTS(text=text, lang='hi', slow=False)
  file_name= ''.join(file_name.split(".")[:-1])
  file_path = f"files/" + file_name +  ".mp3"
  tts.save("./static/" + file_path)
  
  return file_path