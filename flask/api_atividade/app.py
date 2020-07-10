from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
  def get(self, nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    try:
      response = {
        'nome': pessoa.nome,
        'idade': pessoa.idade,
        'id': pessoa.id
      }
    except AttributeError:
      response = {
        'status': 'error',
        'msg': 'Pessoa não encontrada!'
      }
    return response
  
  def post(self, nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    dados = request.json
    print(dados)
    return {'nome':'Diogo'}


api.add_resource(Pessoa, '/pessoa/<string:nome>/')

if __name__ == "__main__":
    app.run(debug=True)