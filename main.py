from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('lomake.html')

@app.route("/vastaus")
def vastaus():
    salaus=request.args['salauksen_muokkaus']
    salattu=request.args['nimi']
    for i in range(1,len(salaus),2):
        salattu = salattu.replace(salaus[i],salaus[i-1])
    
    return render_template('vastaus.html', nimi=request.args['nimi'], tulos=salattu, purku=salaus[::-1])
    

if __name__ == '__main__':
    app.run()