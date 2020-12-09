from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/video', methods = ['GET', 'POST'])
def streaming_video():
    if request.method == 'POST':
        name = request.form['name']
        app.logger.debug(name)
        return send_file('uploads/videos/'+name+'.mp4', mimetype='video/mp4')

    if request.method == 'GET':
        return "not proper access"


@app.route('/getImage', methods = ['GET', 'POST'])
def get_user_image():
    if request.method == 'POST':
        name = request.form['name']
        app.logger.debug(name)
        f_image = request.files['picture']
        f_audio = request.files['audio']
        f_image.save('./uploads/images/' + name + '.png')
        f_audio.save('./uploads/records/' + name + '.m4a')
	


    if request.method == 'GET':
        return "not proper access"


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    app.logger.debug('message')
    app.logger.waring('warning!!')
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
