from flask import Flask, request
from controllers.note import note_router
from services.csv_service import add_note, get_note, update_note, delete_note

app = Flask(__name__)

app.register_blueprint(note_router)

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Notes App!'

if __name__ == '__main__':
    app.run(debug=True)