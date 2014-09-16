from flask import Blueprint
from flask.ext.restful import Api
from .endpoints.goal import Goal
from .endpoints.weight import Weight
from .endpoints.calories import Calories

api_blueprint = Blueprint('api', __name__)
api = Api(prefix='/api/v1.0')

# Register the endpoints
api.add_resource(Goal, '/goal', '/goal')
api.add_resource(Weight, '/weight/<string:id>', '/weight')
api.add_resource(Calories, '/calories/<string:id>', '/calories')