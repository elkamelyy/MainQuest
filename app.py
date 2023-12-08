from flask import Flask, jsonify, request, render_template
import bing
app = Flask(__name__)


#model=pickle.load(open('/content/drive/MyDrive/projects/flask/model','rb'))
@app.route('/', methods=['GET'])
def index():
  return render_template("Interface.html")

@app.route("/predict",methods=["POST"])
def predict():
  if request.method == 'POST':
    #print(input_values)

    s=bing.proccess_input(str(request.form.get('recheche')))


    return jsonify({"prediction":s})

  #return jsonify({"reponse":"erreur"})




if __name__ == '__main__':
    app.run()


