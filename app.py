from flask import Flask
from flask_graphql import GraphQLView
from src.schema import schema


app = Flask(__name__)
app.config.from_pyfile('.env')

# Configuração da rota do 'graphql'
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.before_first_request
def create_db():
   db.create_all()

@app.route('/')
def index():
    return '<p> Hello World</p>'

if __name__ == '__main__':
    from data.database import db
    db.init_app(app)
    app.run()
