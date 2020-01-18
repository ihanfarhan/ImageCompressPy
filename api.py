from config import SERVER_IP, SERVER_PORT
from app import create_app

app = create_app(debug=True)

if __name__ == '__main__':
    app.run(host=SERVER_IP, port=int(SERVER_PORT), debug=True, threaded=True)
