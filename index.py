from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/todayhomework', methods=['GET'])
def show_homework():
    try:
        with open("homework.txt", "r", encoding='utf-8') as f:
            content = f.read()
        return render_template('homework.html', content=content)  # 使用模板渲染内容
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "Homework not found."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8964)
