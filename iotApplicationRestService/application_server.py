from flask import render_template
import config

# Get the application instance
connex_app = config.connex_app

#Read file swagger
connex_app.add_api("swagger.yml")

#Run in stand alone mode
if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=5000, debug=False)
