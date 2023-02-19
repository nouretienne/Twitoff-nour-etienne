from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list
    of ditionaries, so they can be return as JSON
    
    Param: database_records (a list of db.Model instances)
    
    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
                {"id":1, "title":"Book 1"},
                {"id":2, "title":"Book 2"},
                {"id":3, "title":"Book 3"}
        ]
    """
    parse_records = []
    for record in database_records:
        print('record:',record)
        parse_record = record.__dict__
        print('parsed_record["_sa_instance_state"]', parse_record["_sa_instance_state"])
        del parsed_record["_sa_instance_state"]
        parse_records.append(parse_record)
    return parse_records