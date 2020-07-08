from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
  {'id': '0',
   'nome':'Diogo',
   'habilidades':['Python', 'Flask']},
  {'id': 1,
   'nome':'Thiago',
   'habilidades':['Python', 'Django']}
]

class Desenvolvedor(Resource):
  def get(self, id):
    try:
      response = desenvolvedores[id]
    except IndexError:
      mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
      response = {'status':'erro', 'mensagem':mensagem}  
    except Exception:
      mensagem = 'Erro desconhecido. Procure o administrador da API!'
      response = {'status':'erro', 'mensagem':mensagem}
    return response
  def put(self):
    return {'nome':'Diogo'}
  def delete(self):
    return {'nome':'Diogo'}

api.add_resource(Desenvolvedor, '/dev/<id>/')

if __name__ == "__main__":
  app.run(debug=True)