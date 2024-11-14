import os
from flask import Flask
from controllers.mutant_controller import mutant_bp
from database.db_connection import init_db

app = Flask(__name__)

init_db()

app.register_blueprint(mutant_bp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)