from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

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
  
  def put(self, nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    dados = request.json
    if 'nome' in dados:
      pessoa.nome = dados['nome']
    if 'idade' in dados:
      pessoa.idade = dados['idade']
    pessoa.save()
    response = {
      'id' : pessoa.id,
      'nome' : pessoa.nome,
      'idade' : pessoa.idade
    }
    return response
  
  def delete(self, nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.delete()
    msg = '{} excluído(a) com sucesso'.format(pessoa.nome)
    return{
      'status':'sucesso',
      'msg':msg
    }

class ListaPessoas(Resource):
  def get(self):
    pessoas = Pessoas.query.all()
    dados = request.json
    response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
    atividade = Atividades(nome=dados['nome'], pessoa=dados['pessoa'])
    atividade.save()
    return response
  
  def post(self):
    dados = request.json
    pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
    pessoa.save()
    response = {
        'id' : pessoa.id,
        'nome' : pessoa.nome,
        'idade' : pessoa.idade
      }
    return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')

if __name__ == "__main__":
    app.run(debug=True)