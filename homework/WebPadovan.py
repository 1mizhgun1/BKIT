from flask import Flask, request
from Padovan import Padovan

app = Flask(__name__)

@app.route('/padovan', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        n = int(request.form.get('N'))
        return '''
                    <h1>Num is: {}</h1>
                    <h2>First {} Padovan`s numbers are:</h2>
                    <h3>{}</h3>'''.format(n, n, ', '.join([str(elem) for elem in Padovan(n)]))

    return '''
              <form method="POST">
                  <div><label>Input N: <input type="text" name="N"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

if __name__ == "__main__":
    app.run(debug=True)