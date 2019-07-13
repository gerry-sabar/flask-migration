from main import app
from flask_restplus import Api, Resource, fields

api = Api(app, doc='/docs')

# our base API path will be {BASE_URL}/my_api
name_space = api.namespace('my_api', description='API Project')

@name_space.route("/")
class LogList(Resource):
    def get(self):  # will be used to fetch all record from log later
        return {
            "status": "List all log"
        }

    def post(self):  # will be used to create a new log record
        return {
            "status": "Create new log"
        }


@name_space.route("/<int:id>")
class LogDetail(Resource):
    def get(self, id):  # will be used to see one particular log detail
        return {
            "status": "See detail for log with id " + str(id)
        }

    def put(self, id):  # will be used to update particular log
        return {
            "status": "Updated log with id " + str(id)
        }

    def delete(self, id):  # will be used to delete particular log
        return {
            "status": "Deleted log with id " + str(id)
        }