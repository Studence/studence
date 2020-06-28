import flask
import os

from flask import request, Response

from CommonCode.RunMainModule.RunFromMAinModule import RunFromMAinModule
from OrganisationModule.OrganisationService import OrganisationService
from Protobuff.organisationUiPb_pb2 import OrganisationUiPb, OrganisationSearchRequestUiPb
from Protobuff.schoolUiPb_pb2 import SchoolUiPb, SchoolSearchRequestUiPb
from RequestHandlerModule.RequestHandler import RequestHandler
from SchoolModule.SchoolService import SchoolService

application = flask.Flask(__name__)
m_runFromMainModule = RunFromMAinModule()
m_runFromMainModule.setRunFromMainModule()


# Only enable Flask debugging if an env var is set to true
# application.debug = os.environ.get('FLASK_DEBUG') in ['true', 'True']

# Get application version from env
# app_version = os.environ.get('APP_VERSION')

# Get cool new feature flag from env
# enable_cool_new_feature = os.environ.get('ENABLE_COOL_NEW_FEATURE') in ['true', 'True']

@application.route('/test')
def hello_world():
    # return str("query" in request.full_path.replace(request.path,''))
    return request.args.get('query')


@application.route('/organisation', methods=['GET', 'POST', 'PUT'])
def organisation():
    requestHandler = RequestHandler(OrganisationService(), OrganisationUiPb(), OrganisationSearchRequestUiPb())
    return requestHandler.handle(request=request)


@application.route('/school', methods=['GET', 'POST', 'PUT'])
def school():
    requestHandler = RequestHandler(SchoolService(), SchoolUiPb(), SchoolSearchRequestUiPb())
    return requestHandler.handle(request=request)


if __name__ == '__main__':
    application.run(host='127.0.0.1')
