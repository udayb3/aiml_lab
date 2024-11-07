from flask import Flask as flask, render_template, request
import pickle

with open('./ques_list.pkl' , 'rb') as f:
  ques = pickle.load(f)


with open('./similarity.pkl' , 'rb') as f:
  sim = pickle.load(f)

# __name__ is a special attribute which is equal to the part of the program which is running.
app= flask(__name__)

# The route function is a type of python decorator.
@app.route('/')
def home():
  return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
  data= request.form
  inp= data['qName']
  index = ques[ques['name'] == inp].index[0]
  distances = sorted(list(enumerate(sim[index])),reverse=True,key = lambda x: x[1])
  return {
    str(i): ques.iloc[i[0]]['name'] for i in distances[1:6]
  }