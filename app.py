from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_alunos():
    lista = [
    (1, 'Wesley Gabriel Santos', 18, 'Teresina'),
    (2, 'Ana Beatriz Oliveira', 20, 'Parnaíba'),
    (3, 'João Victor Lima', 19, 'Picos'),
    (4, 'Maria Vitória Costa', 21, 'Floriano'),
    (5, 'Lucas Henrique Alves', 18, 'Piripiri'),
    (6, 'Clara Fernanda Rodrigues', 22, 'Campo Maior'),
    (7, 'Pedro Lucas Carvalho', 20, 'Teresina'),
    (8, 'Isadora Martins Souza', 19, 'Parnaíba'),
    (9, 'Matheus Gabriel Pereira', 23, 'Picos'),
    (10, 'Laura Beatriz Santos', 18, 'Floriano'),
    (11, 'Gabriel Henrique Costa', 21, 'Teresina'),
    (12, 'Sophia Rodrigues Lima', 20, 'Piripiri'),
    (13, 'Arthur Miguel Oliveira', 19, 'Campo Maior'),
    (14, 'Manuela Alves Ferreira', 22, 'Parnaíba'),
    (15, 'Enzo Gabriel Martins', 21, 'Teresina'),
    (16, 'Rafael Henrique Souza', 20, 'Picos'),
    (17, 'Bianca Vitória Almeida', 19, 'Floriano'),
    (18, 'Gustavo Lucas Pereira', 22, 'Teresina'),
    (19, 'Júlia Martins Costa', 18, 'Parnaíba'),
    (20, 'Felipe Augusto Santos', 23, 'Piripiri'),
    (21, 'Mariana Alves Rodrigues', 20, 'Teresina'),
    (22, 'Daniel Henrique Lima', 21, 'Campo Maior'),
    (23, 'Beatriz Fernanda Souza', 19, 'Picos'),
    (24, 'Caio Gabriel Oliveira', 22, 'Floriano'),
    (25, 'Luana Vitória Santos', 18, 'Teresina'),
    (26, 'Henrique Martins Carvalho', 24, 'Parnaíba'),
    (27, 'Amanda Ferreira Lima', 20, 'Piripiri'),
    (28, 'Leonardo Gabriel Alves', 21, 'Teresina'),
    (29, 'Helena Rodrigues Costa', 19, 'Campo Maior'),
    (30, 'Bruno Henrique Pereira', 22, 'Picos'),
    (31, 'Carolina Beatriz Martins', 20, 'Floriano'),
    (32, 'Samuel Lucas Oliveira', 18, 'Teresina'),
    (33, 'Letícia Alves Santos', 21, 'Parnaíba'),
    (34, 'Vinícius Gabriel Costa', 23, 'Piripiri'),
    (35, 'Alice Vitória Rodrigues', 19, 'Teresina'),
    (36, 'Nicolas Henrique Lima', 20, 'Picos'),
    (37, 'Melissa Fernanda Souza', 22, 'Campo Maior'),
    (38, 'João Pedro Almeida', 18, 'Floriano'),
    (39, 'Yasmin Oliveira Santos', 21, 'Teresina'),
    (40, 'Murilo Gabriel Costa', 23, 'Parnaíba'),
    (41, 'Eduarda Martins Lima', 19, 'Piripiri'),
    (42, 'Rodrigo Henrique Alves', 22, 'Teresina'),
    (43, 'Valentina Souza Pereira', 20, 'Picos'),
    (44, 'Miguel Lucas Rodrigues', 18, 'Campo Maior'),
    (45, 'Nicole Beatriz Costa', 21, 'Floriano'),
    (46, 'Thiago Gabriel Santos', 23, 'Teresina'),
    (47, 'Rebeca Vitória Lima', 19, 'Parnaíba'),
    (48, 'Davi Henrique Oliveira', 20, 'Piripiri'),
    (49, 'Lorena Martins Alves', 22, 'Teresina'),
    (50, 'Vitor Gabriel Pereira', 21, 'Picos')
    ]
    return render_template('aluno/lista_aluno.html', lista=lista)


@app.route('/professor')
def listar_professores():
    lista = [
    (1, 'Diego Henrique Martins', 34, 'Teresina'),
    (2, 'Larissa Beatriz Costa', 27, 'Parnaíba'),
    (3, 'Ruan Gabriel Oliveira', 39, 'Picos'),
    (4, 'Letícia Alves Pereira', 31, 'Floriano'),
    (5, 'André Victor Santos', 43, 'Piripiri'),
    (6, 'Marina Carvalho Lima', 29, 'Campo Maior'),
    (7, 'Guilherme Rodrigues Souza', 36, 'Teresina'),
    (8, 'Natália Ferreira Alves', 33, 'Parnaíba'),
    (9, 'Caio Henrique Costa', 28, 'Picos'),
    (10, 'Bruna Martins Oliveira', 41, 'Floriano'),
    (11, 'Samuel Pereira Santos', 35, 'Teresina'),
    (12, 'Eduarda Vitória Lima', 26, 'Piripiri'),
    (13, 'Leonardo Almeida Costa', 44, 'Campo Maior'),
    (14, 'Melissa Rodrigues Silva', 30, 'Parnaíba'),
    (15, 'Victor Gabriel Ferreira', 38, 'Teresina')
    ]
    return render_template('professor/lista_professor.html', lista=lista)



@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

if __name__ == '__main__':
    app.run(debug=True)