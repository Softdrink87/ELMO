from flask import Flask
from flask import request,render_template
from flask import jsonify
from predic import Predict

app = Flask(__name__)
mdl = Predict()

@app.route('/test')
def test():
    return render_template('main.html')

@app.route('/QA',methods=["POST"])
def qa() -> str:
    #received_data = request.get_json(force=True)
    form_x = request.form['theme']
    form_y = request.form['sentence']
    form_link = request.form['link']
    received_theme, received_sentence, received_link = form_x, form_y, form_link
    result = mdl.predict(mdl, received_theme, received_sentence, received_link)
    return result

if __name__ == '__main__':  # if it's an entry point. then run Flask :O -> if it's not a module call then run Flask :D
    app.run(host='0.0.0.0', port=5000,debug=True)

