from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello from Music AI Backend!"

@app.route('/api/generate_music', methods=['POST'])
def generate_music():
    data = request.json
    prompt = data.get('prompt', 'No prompt provided')
    lyrics = data.get('lyrics', '')
    sound_description = data.get('soundDescription', '')
    is_instrumental = data.get('isInstrumental', False)
    song_name = data.get('songName', 'Generated Song')

    print(f"Received request: Prompt='{prompt}', Lyrics='{lyrics}', Instrumental={is_instrumental}")

    generated_song_url = "https://example.com/dummy_song.mp3"

    response_data = {
        "success": True,
        "message": "Dummy song generated successfully!",
        "song": {
            "id": 12345,
            "name": f"AI Song: {song_name}",
            "url": generated_song_url,
            "duration": "2:55",
            "genre": "AI Generated",
            "instrumental_only": is_instrumental
        }
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
