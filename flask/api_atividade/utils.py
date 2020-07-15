from models import Pessoas

def insere_pessoas():
  pessoa = Pessoas(nome='Diogo', idade='38')
  print(pessoa)
  pessoa.save()

def consulta_pessoas():
  pessoas = Pessoas.query.all()
  print(pessoas)
  #pessoa = Pessoas.query.filter_by(nome='Diogo').first()
  #print(pessoa.idade)

def altera_pessoa():
  pessoa = Pessoas.query.filter_by(nome='Diogo').first()
  pessoa.idade = 30
  pessoa.save()

def exclui_pessoa():
  pessoa = Pessoas.query.filter_by(nome='Thiago').first()
  pessoa.delete()



if __name__ == "__main__":
  insere_pessoas()
  consulta_pessoas()
  #altera_pessoa()
  #exclui_pessoa()