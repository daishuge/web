from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# 获取当前文件的目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['POST'])
def receive_data():
    # 获取JSON数据
    data = request.get_json()
    print("接收到的数据:", data)
    test = data['text']

    # 写入文件
    with open(os.path.join(BASE_DIR, "homework.txt"), "w") as f:
        f.write(test)

    # 返回响应
    return jsonify({"status": "success", "message": "Homework saved successfully"})

@app.route('/download_homework', methods=['GET'])
def download_homework():
    # 发送文件给客户端
    return send_from_directory(directory=BASE_DIR, path='homework.txt', as_attachment=True)

@app.route('/todayhomework', methods=['GET'])   # 添加路由
def show_homework():
    try:
        with open("homework.txt", "r", encoding='utf-8') as f:  # 确保以UTF-8编码打开文件
            content = f.read()
        return content, 200, {'Content-Type': 'text/plain; charset=utf-8'}  # 指定响应的字符集为UTF-8
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "Homework not found."})
    
################ gpt ############

# import openai
# import time

# client = openai.OpenAI(api_key="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")

# def gpt(history,模型="gpt-3.5-turbo", 打印=True):

#     响应 = client.chat.completions.create(
#         # 模型='gpt-4-1106-preview',
#         # 模型="gpt-3.5-turbo",
#         model=模型,
#         messages=history,
#         temperature=1,
#         max_tokens=1000,
#         stream=True
#     )

#     结果 = ""

#     for 部分 in 响应:
#         内容 = 部分.choices[0].delta.content if 部分.choices[0].delta and 部分.choices[0].delta.content else ""
#         结果 += 内容
#         if 打印:
#             print(内容, end='', flush=True)

#     return 结果

# http_return=[]
# # 格式： 
# # [
# #     {"uuid":uuid,"ask":ask,"reply":"None","status":"waiting","time":时间戳},
# #     {"uuid":uuid,"ask":ask,"reply":reply,"status":"done","time":时间戳}
# # ]

# history={}
# # 格式
# # {
# #   "uuid1": [
# #     {"role": "system", "content": "you are a helpful assistant"},
# #     {"role": "user", "content": "hello"}
# #   ],
# #   "uuid2": [
# #     {"role": "system", "content": "you are a helpful assistant"},
# #     {"role": "user", "content": "hello"}
# #   ]
# # }


# @app.route('/gpt_upload', methods=['POST'])
# def postdata():
#     data = request.json
#     now=time.time()
#     uuid=data["uuid"]
#     ask=data["ask"]
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)