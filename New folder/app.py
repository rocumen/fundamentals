from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    expression = ''
    result = ''
    
    if request.method == 'POST':
        expression = request.form['expression']
        btn = request.form['btn']

        if btn == '=':
            try:
                result = str(eval(expression))
                expression = result
            except:
                result = 'Error'
                expression = ''
        elif btn == 'C':
            expression = ''
        else:
            expression += btn
    
    return render_template('index.html', expression=expression, result=result)

if __name__ == '__main__':
    app.run(debug=True)
