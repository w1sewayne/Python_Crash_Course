# 保存为 my_web.py
from flask import Flask

# 创建一个网站应用
app = Flask(__name__)

# 告诉 Python，当用户访问首页 '/' 时，执行下面的函数
@app.route('/')
def home():
    # 这里返回的是 HTML 代码 (网页的骨架)
    return '''
    <div style="text-align: center; padding: 50px;">
        <h1 style="color: #336699;">👋 你好！这是我的 Python 个人主页</h1>
        <hr>
        <p>我现在正在学习 Python 编程。</p>
        <p>这是我创建的第一个网页应用！</p>
        <button>点击这里没反应，因为我还不会写JavaScript😂</button>
    </div>
    '''

# 启动网站服务器
if __name__ == '__main__':
    print("网站已启动！请在浏览器访问: http://127.0.0.1:5000")
    app.run(debug=True)