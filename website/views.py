from website import app
from flask import Flask, render_template, url_for
from models import *
import os

# don't use models.Post, use Post
# don't forget to check permissions

@app.route('/index.html')
@app.route('/home')
@app.route('/')
def home():
    return render_template('aboutme.html', title='About')

@app.route('/about')
def about():
	return render_template('aboutme.html', title='About')

@app.route('/post')
def post():
	cat = Category.query.all()
	cat = cat[0]
	bodypath = ("/home/brady/website/website/posts/resistor-divider.html")
	postbody = open(bodypath, 'r').read()
	testPost = Post(title='Example Title', body=postbody, category=cat)
	return render_template('post.html', post=testPost, title=testPost.title)

@app.route('/shivani')
def shivani():
	return render_template('aboutugly.html', title='Ugly')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/blogtest')
def blogex():
    return render_template('index.html')

@app.route('/svgtest')
def svg():
	return render_template('svgtest.html')