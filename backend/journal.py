from flask_restx import Namespace, Resource, fields, marshal_with
from dbmodels import Journal 
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from datetime import datetime

""" Journal
    returns journals of users 
"""

journal_ns = Namespace('journal', description= "a namespace for journals")

"""
    Journal Model
"""

journal_model = journal_ns.model(
    "Journal",
    {
        "journal_id" : fields.Integer(),
        "date": fields.Date(),
        "title": fields.String(),
        "description": fields.String(),
        "username": fields.String()
    }
)

@journal_ns.route('/journals')
class Journalresource_multi(Resource):

    @journal_ns.marshal_list_with(journal_model)
    def get(self):
        """ gets all journals from DB """
        journals = Journal.query.all()
        return journals
    
    @journal_ns.marshal_with(journal_model)
    @journal_ns.expect(journal_model)
    @jwt_required()
    def post(self):
        """ Create a new Journal """
        current_user = get_jwt_identity()
        data = request.get_json()
        date = datetime.now().strftime("%Y-%m-%d")
        new_journal = Journal(
            title = data.get('title'),
            date = date,
            description = data.get('description'),
            username = current_user
        )
        new_journal.save()

        return new_journal, 201
    
 
@journal_ns.route('/journal_edit')
class Journalresource(Resource):
    @jwt_required()
    @journal_ns.marshal_with(journal_model)
    def put(self):
        """ with username as field update journal"""
        current_user = get_jwt_identity()
        print(f"{current_user}")
        update_db = Journal.query.filter_by(username = current_user).first()
        data = request.get_json()
        update_db.title = data.get('title')
        update_db.description = data.get('description')
        update_db.date = datetime.now().strftime("%Y-%m-%d")
        update_db.save()
        return update_db
    