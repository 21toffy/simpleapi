from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from time import time



#init
app = Flask(__name__)


app.config['SECRET_KEY'] = 'thisissecretkey'
# app.config.from_object(Config)
basedir = os.path.abspath(os.path.dirname(__file__))

#Databse
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "db.sqlite") + 'bucketlist.db'



db = SQLAlchemy(app)



#post Class/model

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title =db.Column(db.String(140))
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())





# to get single post(POST request)
@app.route('/post/<id>', methods=["GET"])
def get_singlepost(id):
	post = Post.query.filter_by(id=id).first()
	if not post:
		return jsonify({"error":"No Post was found"})
	post_data = {}
	post_data["id"] = post.id
	post_data["title"] = post.title
	post_data["body"] = post.body
	post_data["created"] = post.created
	    
	return jsonify({"post":post_data})








# to list out posts(GET)
@app.route('/', methods=["GET"])
def list_of_posts():
    posts = Post.query.all()
    output = []
    for post in posts:
        post_data = {}
        # post_data["id"] = post.id
        post_data["title"] = post.title
        post_data["body"] = post.body
        post_data["created"] = post.created
        output.append(post_data)
        
    return jsonify({"posts":output})




# to create post(POST request)
@app.route('/add-post', methods=["POST"])
def create_post():
    data = request.get_json()

    new_post = Post(title = data['title'], body = data['body'] )
    db.session.add(new_post)
    db.session.commit()

    return ({"message":"New post created"})





#runserver
if __name__ == '__main__':
    app.run(debug=True)




