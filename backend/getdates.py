"""
GET predictions

    after login 
    - get data 
"""
from flask import request
from dbmodels import Userdates
from calculate import Calculate_date
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
date_ns = Namespace('dates', description="handles all logic of dates")

dates_model = date_ns.model(
     "Dates",
     {
        "fdlp":fields.Date(),
        "acd":fields.Integer(),
        "next_period_date":fields.Date(),
        "fertile_window_start":fields.Date(),
         "fertile_window_end":fields.Date(), 
        "ovulation_date":fields.Date(), 
        "preg_test_date":fields.Date(),
        "username": fields.String(),
        "usr_id" : fields.Integer()
     }
)

@date_ns.route('/date')
class DateResources_multi(Resource):

    @date_ns.marshal_list_with(dates_model)
    def get(self):
        """Get all dates belonging to username"""
        dates = Userdates.query.all()
        return dates
    
    @date_ns.marshal_with(dates_model)
    @date_ns.expect(dates_model)
    @jwt_required()
    def post(self):
        """Create a Date"""
        data = request.get_json()
        fdlp = data.get('fdlp')
        acd = data.get('acd')
        current_user = get_jwt_identity()
        new_date = Userdates(
            username = current_user,
            fdlp = fdlp,
            acd = acd,
            next_period_date = Calculate_date(fdlp, acd).next_period_date(),
            fertile_window_start = Calculate_date(fdlp, acd).fertile_window_start_day(),
            fertile_window_end = Calculate_date(fdlp, acd).fertile_window_end_day(),
            ovulation_date = Calculate_date(fdlp, acd).ovulation_date(),
            preg_test_date = Calculate_date(fdlp, acd).take_pregnancy_test(),
        )
        new_date.save()

        return new_date, 201