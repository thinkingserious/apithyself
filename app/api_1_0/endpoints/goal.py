from flask.ext.restful import Resource, abort, fields, marshal_with, reqparse
from ..models import HealthGoal
from ..models import db

# Documentation for this endpoint: http://docs.apithyself.apiary.io
resource_fields = {
    'date':     fields.String,
    'weight':   fields.Integer
}

class Goal(Resource):
    def __init__(self):
        super(Goal, self).__init__()
    
    @marshal_with(resource_fields)
    def get(self):
        ret = HealthGoal.query.first()
        return ret, 200
        
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str)
        parser.add_argument('weight', type=int)
        args = parser.parse_args()
        ret = HealthGoal.query.first()

        if ret != None:
            abort(400, error="400", message="Goal already exists. Use PATCH to modify.")

        ret.date = args['date']
        ret.weight = args['weight']
        db.session.add(ret)
        db.session.commit()
        return args, 201

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str)
        parser.add_argument('weight', type=int)
        args = parser.parse_args()

        if ( args['date'] or args['weight']) == None:
            abort(400, error="400", message="Missing argument, date or weight.")

        ret = HealthGoal.query.first()

        if args['date'] != None:
            ret.date = args['date']
        if args['weight'] != None:
            ret.weight = args['weight']

        db.session.add(ret)
        db.session.commit()
        return args, 204