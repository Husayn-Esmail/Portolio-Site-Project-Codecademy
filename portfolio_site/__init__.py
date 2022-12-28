

def create_app(config_filename):
    from .routes import app
    app.config.from_pyfile(config_filename)

    return app


# from flask import Flask, render_template
# import os
# # from recursive.recursive_indexer import get_projects_for_display

# # def create_app(test_config=None):
# def create_app(config_filename):
#     # create and configure the app
#     # app = Flask(__name__, instance_relative_config=True)
#     app = Flask(__name__, instance_path='/Portolio-Site-Project-Codecademy/instance', instance_relative_config=True)
#     app.config.from_pyfile(config_filename)
#     # app.config.from_pyfile(test_config)
#     # app.config.from_object('default_settings')
#     # app.config.from_envvar('PORTFOLIO_SETTINGS')
#     # app.config.from_mapping(
#     #     FLASK_ENV="development",
#     #     FLASK_DEBUG=True,
#     #     FLASK_RUN_HOST="0.0.0.0",
#     #     FLASK_RUN_PORT=5500,
#     #     TEMPLATES_AUTO_RELOAD=True,
#     #     SECRET_KEY='dev',
#     #     FLASK_APP="portfolio_site"
#     # )
#     # print("create_app")
#     # not setting up a database
#     # if test_config is None:
#     #     # load the instance config, if it exists, when not testing
#     #     app.config.from_pyfile('config.py', silent=True)
#     # else:
#     #     # load the test config if passed in
#     #     app.config.from_mapping(test_config)
#         # app.config.from_pyfile(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     @app.route('/', methods=['GET'])
#     def index():
#         image_path = "portfolio_site/static/img"
#         desc_path = "portfolio_site/static/descriptions"
#         ignored = ['favicons', 'hero', '.DS_Store']
#         projects = recursive_indexer.get_projects_for_display(image_path, desc_path, ignored)
#         # the projects out of read_images are not json serializable, must be
#         # converted first.
#         json_projects = []
#         for project in projects:
#             json_projects.append(project.to_json())
#         data = json_projects
#         return render_template('index.html', data=data)

#     @app.route('/contact', methods=['GET', 'POST'])
#     def contact():
#         return render_template('contact.html')

#     @app.route('/test', methods=['GET'])
#     def test():
#         return render_template('test.html')
    
#     @app.route('/resume', methods=["GET"])
#     def resume():
#         return render_template("resume.html")


#     return app

# # if __name__ == '__main__':
# #     app = create_app()
# #     server = Server(app.wsgi_app)
# #     # server.watch('./templates/*')
# #     server.serve(host='0.0.0.0')