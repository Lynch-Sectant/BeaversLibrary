from flask import Flask
import os

app = Flask(__name__)

@app.route('/create_a_book', methods=['GET', 'POST'])
def new_book():
    form = UploadForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('upload.html', title='Добавить книгу', form=form)

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
