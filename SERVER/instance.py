from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    self.app = Flask(__name__)
    self.blueprint = Blueprint('api', __name__, url_prefix='/api')
    self.api = Api(self.blueprint, doc = '/doc', title='Conversor de Câmbio')