from transformers import AutoModelForCausalLM, AutoProcessor
from PIL import Image

def get_caption(img_path):
  task_prompt= "<DETAILED_CAPTION>"
  image = Image.open(img_path).convert("RGB")
  
  model = AutoModelForCausalLM.from_pretrained("thwri/CogFlorence-2-Large-Freeze", trust_remote_code=True).to('cpu').eval()
  processor = AutoProcessor.from_pretrained("thwri/CogFlorence-2-Large-Freeze", trust_remote_code=True)
  
  inputs = processor(text= task_prompt, images=image, return_tensors="pt").to('cpu')
  generated_ids = model.generate( input_ids=inputs["input_ids"], pixel_values=inputs["pixel_values"], max_new_tokens= 32, num_beams=3, do_sample=True )
  generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
  parsed_answer = processor.post_process_generation(generated_text, task=task_prompt, image_size=(image.width, image.height))
  
  del model
  del processor
  
  return parsed_answer['<DETAILED_CAPTION>']