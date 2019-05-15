from flask import render_template
import connexion

#Application instance
app = connexion.App(__name__, specification_dir="./")

#Read file swagger
app.add_api('swagger.yml')

#URL route for "/"
@app.route('/')
def home():
    return render_template('home.htm')

#Run in stand alone mode
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
