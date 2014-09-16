from flask.ext.restful import Resource, abort, fields, marshal_with, reqparse
from ..models import HealthWeight
from ..models import db

# Documentation for this endpoint: http://docs.apithyself.apiary.io

resource_fields = {
    'date':     fields.String,
    'weight':   fields.Integer
}

class Weight(Resource):
    def __init__(self):
        super(Weight, self).__init__()

    @marshal_with(resource_fields)
    def get(self, id=None):
        if id == None:
            ret = HealthWeight.query.all()
        else:
            ret = HealthWeight.query.filter_by(date=id).first()
            if ret == None:
                abort(400, error="400", message="There is no entry on that date.")
        return ret, 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str)
        parser.add_argument('weight', type=int)
        args = parser.parse_args()
        ret = HealthWeight.query.filter_by(date=args['date']).all()

        if ret:
            abort(400, error="400", message="You already logged your weight today. Use PATCH to modify.")

        ret = HealthWeight(date=args['date'], weight=args['weight'])
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

        ret = HealthWeight.query.first()
        ret.date = args['date']
        ret.weight = args['weight']
        db.session.add(ret)
        db.session.commit()
        return args, 204