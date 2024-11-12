from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model
with open('marksmodel.pickle', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get input values from the form
            marks1 = int(request.form['marks1'])
            marks2 = int(request.form['marks2'])
            
            # Predict 3rd MST marks using the model
            prediction = model.predict(np.array([[marks1, marks2]]))
            predicted_marks = round(prediction[0], 2)  # Round to 2 decimal places
        except Exception as e:
            predicted_marks = f"Error: {str(e)}"
        
        return render_template('index.html', predicted_marks=predicted_marks, marks1=marks1, marks2=marks2)
    
    return render_template('index.html', predicted_marks=None)

if __name__ == '__main__':
    app.run(debug=True)
