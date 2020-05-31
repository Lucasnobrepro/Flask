# Importar classes
from flask import Flask
from flask_restful import Api

# Intanciando as classes.
app = Flask(__name__)
api = Api(app)

# Especificando rota como http://127.0.0.1:5000/hello
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# Run Hello World.
if __name__ == '__main__':
    app.run(debug=True)