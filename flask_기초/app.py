from flask import Flask, request, jsonify, render_template
from http.server import HTTPServer, SimpleHTTPRequestHandler

app = Flask(__name__)

@app.route('/')
def home() :
    return render_template('index.html')

posts = [
    {"id": 1, "title": "Post 1", 'content': 'This is post 1'},
    {"id": 2, "title": "Post 2", 'content': 'This is post 2'},
    {"id": 3, "title": "Post 3", 'content': 'This is post 3'}
]

# GET /posts - 모든 게시물 조회
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# GET /posts/<int:post_id> - 특정 게시물 조회
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({"message": "Post not found"}), 404

# POST /posts - 새 게시물 생성
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.json
    new_post["id"] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201

# PUT /posts/<int:post_id> - 특정 게시물 수정
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        updated_data = request.json
        post.update(updated_data)
        return jsonify(post)
    else:
        return jsonify({"error": "Post not found"}), 404

# DELETE /posts/<int:post_id> - 특정 게시물 삭제
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return jsonify({"message": "Post deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
