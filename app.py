from flask import Flask, render_template, request, redirect, send_file, jsonify,url_for
import streamlink

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/terms')
def terms():
    return render_template('terms-and-conditions.html')


@app.route('/download', methods=["POST", "GET"])
def download():
  url = request.form["url"]
  print("Someone just tried to download", url)
  streams = streamlink.streams(url)
  if not streams:
    return redirect(url_for('terms'))
  else:
    stream = streams['best']
    download_url = stream.url
    return redirect(download_url)
    


if __name__ == '__main__':
  app.run(debug=True)
