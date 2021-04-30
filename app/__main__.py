from twitoff_app import create_app

app = create_app()
# with app.app_context():
#     db.create_all()
app.run(debug=True)