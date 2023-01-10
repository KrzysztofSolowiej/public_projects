import joblib
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

def get_pred(avr_temp_C=None):
    model = joblib.load('linear_regression')
    y_pred = model.predict( [[avr_temp_C]] )
    
    return y_pred

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        avr_temp_C = request.values['avr_temp_C']    
        label_pred = get_pred(np.array(avr_temp_C, dtype=float))
        return render_template('index.html', temp=avr_temp_C, result=np.round(np.exp(label_pred)))
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)