from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        birthdate = request.form.get('birthdate')
        if not birthdate:
            error = 'Si us plau, introdueix la teva data de naixement.'
        else:
            from datetime import datetime
            birth_year = int(birthdate.split('-')[0])
            current_year = datetime.now().year
            age = current_year - birth_year
            if age < 18:
                error = '⚠️ Accés denegat! Has de tenir més de 18 anys.'
            else:
                return redirect(url_for('video'))
    return render_template('index.html', error=error)

# Ruta del vídeo
@app.route('/video')
def video():
    return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=True)