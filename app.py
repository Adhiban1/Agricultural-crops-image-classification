from model import prediction
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_type = '-'
    error = ''
    show_image = False
    if request.method == 'POST':
        request.files['file'].save('static/image.jpg')

        try:
            image_type = prediction('static/image.jpg')
        except Exception as e:
            error = e

    if image_type != '-':
        show_image = True
    return render_template('index.html', 
                           image_type=image_type, 
                           show_image=show_image, 
                           error=error)

if __name__ == '__main__':
    app.run(debug=True)

