from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return f'''
<h1>Jeg vet ikke hva jeg skal skrive</h1>
<ul>
    <li><a href="/info">Info om meg</a></li>
    <li><a href="/idk">Jeg vet ikke</a></li>
    <li><a href="/hva">Hva?</a></li>
    <li><a href="/navn">Navnet mitt</a></li>

</ul>
'''

@app.route('/info')
def info():
    return 'info : Jeg vet ikke egt'

@app.route('/idk')
def idk():
    return 'idk : Jeg vet ikke egt igjen'

@app.route('/hva')
def hva():
    return 'hva : Jeg vet ikke egt enda en gang'


if __name__ == "__main__":
    app.run()
