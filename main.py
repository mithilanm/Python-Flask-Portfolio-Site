import flask
from flask import Flask, render_template, request, redirect, url_for, session, flash, Response

app = flask.Flask(__name__)


@app.route('/resume/')
def home():
    return render_template('index.html')


@app.route('/resume/about')
def about():
    return render_template('about.html')


@app.route('/resume/resume')
def resume():
    return render_template('resume.html')


@app.route('/resume/tech-projects')
def tech_projects():
    return render_template('tech-projects.html')


@app.route('/resume/graphic-projects')
def graphic_projects():
    return render_template('graphic-projects.html')


@app.route('/resume/contact')
def contact():
    return render_template('contact.html')
