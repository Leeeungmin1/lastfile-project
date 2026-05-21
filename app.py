from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Docker Hub + Azure ACR 멀티 레지스트리 자동 배포 완료 (과제4)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)