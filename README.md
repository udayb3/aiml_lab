# Image Captioning and Translator
### This project takes the input image and produces an audio file containing the description of the image in your preferred language.  

# TechStack
## Model-Side
- For the image captioning task, I have used [`CogFlorence-2-Large-Freeze`](https://huggingface.co/thwri/CogFlorence-2-Large-Freeze) model.
- Further, IndicTrans2 is used for the translation task, which then further uses gtts to suppot audio.
## Server-Side
- Flask is used to create the website interface.

# Set-up
## To set-up the project locally, follow the instructions given below:
1. Clone the repository
   > git clone https://github.com/udayb3/aiml_lab
2. Ensure that you have python runtime environment with the python version `python3.12`.
3. Next, Create a virtual environment using pip/conda. Usage of pip is shown here.
	> python -m venv myvenv
  -   For Windows:
    > ./myvenv/scripts/activate
  - For Linux:
	> source ./myvenv/bin/activate
4. Clone the Hugging face interface from github
> cd Models
> git clone https://github.com/AI4Bharat/IndicTrans2.git
> cd IndicTrans2/huggingface_interface
> git clone https://github.com/VarunGumma/IndicTransToolkit
> cd IndicTransToolkit
> pip install --editable ./
5. Install the dependencies using:
> pip install -r requirements.txt

