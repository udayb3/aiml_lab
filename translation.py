import torch
from IndicTransToolkit import IndicProcessor
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def translation(text):
  ip = IndicProcessor(inference=True);  src_lan= 'eng_Latn'; tar_lan= 'hin_Deva'
  tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indictrans2-en-indic-dist-200M", trust_remote_code=True)
  model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/indictrans2-en-indic-dist-200M", trust_remote_code=True)
  sentences= [ text ]
  translated_sec= {}

  batch = ip.preprocess_batch(sentences, src_lang= src_lan, tgt_lang= tar_lan)
  batch = tokenizer(batch, padding="longest", truncation=True, max_length=256, return_tensors="pt")
  
  with torch.inference_mode():
      outputs = model.generate(**batch, num_beams=5, num_return_sequences=1, max_length=256)
  
  with tokenizer.as_target_tokenizer():
    outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True, clean_up_tokenization_spaces=True)

  output = ip.postprocess_batch(outputs, lang= tar_lan)
  translated_sec[tar_lan]= output[0]
  
  return translated_sec[tar_lan]