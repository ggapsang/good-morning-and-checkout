from flask import Flask, request, jsonify, render_template
from http.server import HTTPServer, SimpleHTTPRequestHandler

app = Flask(__name__)

@app.route('/')
def home() :
    return render_template('index.html')

# 딥러닝 모델을 대신할 간단한 함수 (실제 모델 호출로 교체 가능)
def dummy_model(prompt):
    return f"Processed: {prompt}"

# 프롬프트를 받아 모델 결과 반환
@app.route('/predict', methods=['POST'])
def predict():
    # 클라이언트에서 보낸 JSON 데이터
    data = request.json
    prompt = data.get('prompt', '')

    # 모델 실행 (여기선 dummy_model 사용)
    result = dummy_model(prompt)

    # 결과 반환
    return jsonify({"prompt": prompt, "result": result})

if __name__ == '__main__':
    app.run(debug=True)