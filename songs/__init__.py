from flask import Blueprint
from flask_restx import Api, Resource

bp = Blueprint('songs', __name__, url_prefix='/song')
api = Api(bp)


model_for_songs = api.parser()
model_for_songs.add_argument('song_name', type=str, required=True)


#All Songs [GET /api/song/all]
@api.route('/all')
class AllSongs(Resource):
    def get(self):
        pass


#Exect Song [GET/ api/song/exect/ {song_name}]
@api.route('/exect')
class ExectlySong(Resource):
    @api.expect(model_for_songs)
    def get(self):
        pass


#Post Song [POST/api/song/post]
@api.route('/post')
class PostSong(Resource):
    def post(self):
        pass


#Put Song [PUT/api/song/put/{song_name}]
@api.route('/put')
class PutSong(Resource):
    @api.expect(model_for_songs)
    def put(self):
        pass


#Delete Song [DELETE/api/song/delete/{song_name}]
@api.route('/delete')
class DeleteSong(Resource):
    @api.expect(model_for_songs)
    def delete(self):
        pass








