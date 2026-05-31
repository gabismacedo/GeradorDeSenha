from main import app
from gerar_senha import gerar_senha
from flask import request, render_template

""""
método get e post, porque o formulário precisa das duas rotas.
O get é quando o navegados abre a página e o POST quando ele envia o código
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    token = None

    if request.method == 'POST':
        # # quantidade = request.form.get(int(input('Digitar código: ')))
        
        quantidade = request.form.get('qtd')
        try:
            quantidade = int(quantidade)
            if quantidade < 1:
                quantidade = 12
            elif quantidade > 30:
                quantidade = 20
        except ValueError:
            quantidade = 12

        token = gerar_senha(quantidade)

    return render_template('index.html', token=token)