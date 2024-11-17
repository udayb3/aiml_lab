from gtts import gTTS

# Convert text to speech
def text_to_speech( text, file_name, lan):
  mapper = { 'hin_Deva': 'hi', 'mar_Deva': 'mr', 'ben_Guru':'bn' }
  tts = gTTS(text=text, lang=mapper[lan], slow=False)
  file_name= ''.join(file_name.split(".")[:-1])
  file_path = f"files/" + file_name +  ".mp3"
  tts.save("./static/" + file_path)
  
  return file_path