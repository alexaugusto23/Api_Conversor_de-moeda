from flask import Flask, Blueprint
from flask_restplus import Api



class Server():
    def __init__(self, ):
        # Registrando App e rotas e views
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc = '/doc', title='Conversor de Câmbio')
        self.app.register_blueprint(self.blueprint)

        # Configurando database
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICANTIONS'] = False

        # 
        self.book_ns = self.book_ns()

        def book_ns(self, ):
            return self.api.namespace(name='Books', description='boos related operations', path='/')

        def run(self,):
            self.app.run(
                port=5000,
                debug=True,
                host='0.0.0.0'
            )

server = Server()