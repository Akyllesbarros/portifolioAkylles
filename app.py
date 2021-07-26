from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message 

app = Flask(__name__)

mail_settings = {

    'MAIL_SERVER' : 'smtp.mailtrap.io',
    'MAIL_PORT' : 2525,
    'MAIL_USERNAME' : '766804a2534515',
    'MAIL_PASSWORD' : 'fb305b0f6aa2af',
    'MAIL_USE_TLS' : True,
    'MAIL_USE_SSL' : False
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato: 
    def __init__(self,  nome, email, msg) :
        self.nome = nome
        self.email = email
        self.msg = msg

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST' :
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['msg']
        )

        msg = Message(
            subject= 'Contato do seu Portifólio',   
            sender= app.config.get("MAIL_USERNAME"),
            recipients=[app.config.get("MAIL_USERNAME")],

            body=f'''O {formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: 
                    {formContato.msg}''' )
        mail.send(msg)
        return redirect('/')
        

if __name__== '__main__' :
    app.run(debug=True)
