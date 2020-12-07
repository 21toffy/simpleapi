from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os


# from models import db, User




app = Flask(__name__)

from models import db, Post





# to list out posts(GET)
@app.route('/', methods=["GET"])
def list_of_posts():
	posts = Post.query.all()
	output = []
	for post in posts:
		post_data = {}
		post_data[id] = post.id
		post_data[title] = post.title
		post_data[body] = post.body
		post_data[created] = post.created
		output.append(post_data)
		
	return jsonify({"posts":output})




# to create post(POST request)
@app.route('/add-post', methods=["POST"])
def create_post():
	data = request.get_json()

	new_post = Post(title = data['title'], body = data['body'] )
	db.session.add(new_post)
	db.session.commit()


	return ({"message":"New user created"})



# to get single post(POST request)
@app.route('/post/<post_id>', methods=["POST"])
def get_singlepost():
	return ''





if __name__ == '__main__':
	app.run(debug=True)
	