from flask.ext.restful import Resource, abort, fields, marshal_with, reqparse
from ..models import HealthCalories
from ..models import db

# Documentation for this endpoint: http://docs.apithyself.apiary.io

resource_fields = {
    'date':     fields.String,
    'calories': fields.Integer
}

class Calories(Resource):
    def __init__(self):
        super(Calories, self).__init__()

    @marshal_with(resource_fields)
    def get(self, id=None):
        if id == None:
            ret = HealthCalories.query.all()
        else:
            ret = HealthCalories.query.filter_by(date=id).first()
            if ret == None:
                abort(400, error="400", message="There is no entry on that date.")
        return ret, 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str)
        parser.add_argument('calories', type=int)
        args = parser.parse_args()
        ret = HealthCalories.query.filter_by(date=args['date']).all()

        if ret != []:
            abort(400, error="400", message="Please use PATCH to add or subtract calories.")

        ret = HealthCalories(date=args['date'], calories=args['calories'])
        db.session.add(ret)
        db.session.commit()
        return args, 201

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str)
        parser.add_argument('calories', type=int)
        args = parser.parse_args()

        if ( args['date'] or args['calories']) == None:
            abort(400, error="400", message="Missing argument, date or weight.")

        ret = HealthCalories.query.first()
        ret.date = args['date']
        ret.calories = ret.calories + args['calories']
        db.session.add(ret)
        db.session.commit()
        return args, 204