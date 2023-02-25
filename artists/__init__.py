from flask import Blueprint
from flask_restx import Api, Resource


bp = Blueprint('artist', __name__, url_prefix='/artist')
api = Api(bp)

model_for_artist = api.parser()
model_for_artist.add_argument('artist_id', type=int, required=True)


#Get All Artists [GET /api/ artist/all]
@api.route('/all')
class AllArtists(Resource):
    def get(self):
        pass


#Get Exectly Artist [GET /api/artist/exect/ {artist_id}]
@api.route('/exect')
class ExectlyArtist(Resource):
    @api.expect(model_for_artist)
    def get(self):
        pass


#Post Artist [POST /api/artist/post]
@api.route('/post')
class PostArtist(Resource):
    @api.expect(model_for_artist)
    def post(self):
        pass


#Put Artist [PUT /api/artist/put/ {artist_id}]
@api.route('/put')
class PutArtist(Resource):
    @api.expect(model_for_artist)
    def put(self):
        pass


#Delete Artist [DELETE /api/artist/delete/  {artist_id}]
@api.route('/delete')
class DeleteArtist(Resource):
    @api.expect(model_for_artist)
    def delete(self):
        pass

