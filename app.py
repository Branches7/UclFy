from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def lista():  # put application's code here
    #TODO
    #Criar um dicionario para produtos com nome, preco e imagem

    lista_tops = {'#1':
                  # NOME     PREÇO     IMAGEM
                      ['Oléo de Soja', 'R$ 1,99',
                       'https://static.clubeextra.com.br/img/uploads/1/350/590350.png'],
                  '#2':
                      ['Leite Italac', 'R$ 2,49', 'https://static.paodeacucar.com/img/uploads/1/194/531194.jpg']
                  }

    return render_template('lista.html', lista_tops=lista_tops)


if __name__ == '__main__':
    app.run()