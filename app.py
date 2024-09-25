from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({
        "version": "v0.0.1-alpha",
        "response": {
                "type": "Text"
        },
        "message": "test message",
        "alive": True
    })

if __name__ == '__main__':
    app.run()
