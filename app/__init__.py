import os
from flask import Flask, render_template,request,jsonify
from app.youtube import youtube_bp
from flask_cors import CORS

from app.gmail import {

    is_email_command,
    extract_email,
    create_gmail_url,
    generate_gmail_with_gemini
}


def create_app():

    app = Flask(__name__)
    CORS(app)

    #youtube
    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    #home
    @app.route("/")
    def home():
        return render_template("index.html")

    #html
    @app.route("/html")
    def html():
        return render_template("index.html")

    #health 
    @app.route("/health")
    def health():
        return jsonify({
            "status":"ok",
            "service":"NOVA AI AGENT"
        })

    # gmail ai agent
    @app.route("/agent",methods["POST"])
    def agent():

        try:
            data=request.get_json(silent=true)or{}
            command=data.get("command","").strip()

    if not command:
        return jsonify({
            "success":false,
            "message":"command is required"
        }),400

    if not is_email_command(command):
        return jsonify({
            "successs":false,
            "message":"please give a Gmail command."
        })400

    recipient=extract_gmail(command)

    email=generate_email_with_gemini(command)

    return jsonify({
        "success":true,
        "type":"email",
        "email_generated":true,
        "recipient":recipient,
        "subject":email["subjuct"],
        "body":email["body"],
        "gmail_url":create_gmail_url(
            email["subject"],
            email["body"],
            recipient
        )
    })

except Expection as e:
return jsonify({
    "success":false,
    "message":str(e)
}),500
    return app
