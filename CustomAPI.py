from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

weather_app = Flask(__name__)
api = Api(weather_app)
weather_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(weather_app)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    # Add other relevant columns (e.g., wind speed, conditions, etc.)

    def __repr__(self):
        return f"Weather(location={self.location}, temperature={self.temperature}, humidity={self.humidity})"


Weather_put_args = reqparse.RequestParser()
Weather_put_args.add_argument("location", type=str, help="Location of the weather data is required", required=True)
Weather_put_args.add_argument("temperature", type=float, help="Temperature of the weather data is required", required=True)
Weather_put_args.add_argument("humidity", type=float, help="Humidity of the weather data is required", required=True)

Weather_update_args = reqparse.RequestParser()
Weather_update_args.add_argument("location", type=str, help="Location of the weather data")
Weather_update_args.add_argument("temperature", type=float, help="Temperature of the weather data")
Weather_update_args.add_argument("humidity", type=float, help="Humidity of the weather data")

class Weather(Resource):
    def get(self, weather_id):
        result = WeatherData.query.filter_by(id=weather_id).first()
        if not result:
            abort(404, message="Error fetching weather data")
        return result

    def put(self, weather_id):
        args = Weather_put_args.parse_args()
        result = WeatherData.query.filter_by(id=weather_id).first()
        if result:
            abort(409, message="Weather data with given ID already exists")
        
        weather = WeatherData(id=weather_id, location=args['location'], temperature=args['temperature'], humidity=args['humidity'])
        db.session.add(weather)
        db.session.commit()
        return weather, 201

    def patch(self, weather_id):
        args = Weather_update_args.parse_args()
        result = WeatherData.query.filter_by(id=weather_id).first()
        if not result:
            abort(404, message="Weather data doesn't exist, unable to update")
        
        if args['location']:
            result.location = args['location']
        if args['temperature']:
            result.temperature = args['temperature']
        if args['humidity']:
            result.humidity = args['humidity']

        db.session.commit(database.db)
        return result

api.add_resource(Weather, '/weather/<int:weather_id>')

if __name__ == "__main__":
    weather_app.run(debug=True)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/')
def index():
    data = {'message': 'Hello, World!'}
    return jsonify(data)


from flask import Flask, jsonify

app = Flask(__name__)

# This is a hypothetical function to fetch weather data using an API key
def get_weather_data(api_key, location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# In your Flask route or elsewhere in your application, you might use this function like this:
@app.route('/weather')
def weather():
    api_key =openweatherapi ='8c2c3caba61078c53199754a8069645f'
    weatherbitapi ='389b04aa3eab4670bae87dfe95be895e'
    accuweatherapi ='TZGWHSw16k008x9f5HkFQ8VBHp5jtz0Y'
    location = request.args.get('location')
    if location:
        weather_data = get_weather_data(api_key, location)
        if weather_data:
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'Failed to fetch weather data'})
        
        if __name__ == "__main__":
         weather_app.run(debug=True, use_reloader=False)
    

    from flask import Flask, request
from flask_restful import Resource, Api, abort
from flask_restful import fields, marshal_with, reqparse
import requests

app = Flask(__name__)
api = Api(app)

# Define fields for serialization
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# Weather API Configuration
weather_api_key = 'YOUR_WEATHER_API_KEY'
weather_api_url = 'http://api.openweathermap.org/data/2.5/weather'

# CRUD Operations for Video Resource
class Video(Resource):

    # GET (READ in CRUD) - Fetches weather data for the city with video ID
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")

        # Fetch weather data
        weather_data = self.fetch_weather(result.name)
        result.weather = weather_data

        return result

    # POST (CREATE in CRUD)
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
   
    # PUT (UPDATE in CRUD)
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()

        return result, 200

    # DELETE (DELETE in CRUD)
    def delete('):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204

    # Fetches weather data for the given city
    def fetch_weather(self, city):
        params = {'q': city, 'appid': weather_api_key, 'units': 'metric'}
        response = requests.get(weather_api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            return {
                'weather_description': weather_description,
                'temperature': temperature,
                'humidity': humidity,
                'wind_speed': wind_speed
            }
        else:
            return {
                'error': 'Failed to fetch weather data'
            }

# Register the Resource called video to the API
api.add_resource(Video, "/video/<int:video_id>")

# Run the API
if __name__ == "__main__":
    app.run(debug=True)

