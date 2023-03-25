from flask import Flask, render_template, request, redirect, send_file
from pytube import YouTube

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
  yt = YouTube(url)
  itag_list = [
    stream.itag
    for stream in yt.streams.filter(file_extension='mp4', progressive=True)
  ]
  download = yt.streams.get_by_itag(int(itag_list[0])).download(filename='{}.mp4'.format(yt.title))
  return send_file('{}.mp4'.format(yt.title), as_attachment=True)


if __name__ == '__main__':
  app.run(port=80, debug=True)
