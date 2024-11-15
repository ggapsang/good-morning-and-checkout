# Flask에서의 경로 변수 사용 방식

## 요청 URL 예시
http://localhost:5000/posts/1  # 이때 1이 post_id로 전달됨

```python
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post["id"] != post_id]
    return jsonify({"message": "Post deleted"}), 200
```
여기서 `post_id`는 특정 게시물의 고유 ID를 의미한다. 즉. 게시물을 식별하는 고유한 ID 값으로, 경로 변수(path parameter)로 사용된다.
클라이언트가 http://localhost:5000/posts/1 같은 URL로 DELETE 요청을 보내면 1이라는 값이 post_id 변수에 전달되어, 이 ID에 해당하는 게시물을 삭제하는 동작을 수행하게 된다

**그렇다면, 각 요청들이 어떤 id를 가지는지, 반대로 각 id가 어떤 요청을 의미하는지를 정리한 메타데이터 같은 문서가 필요하다**

실제로 RESTful API를 설계할 때는 **각 요청의 구조와 의미, 가능한 매개변수 및 ID의 역할** 등을 문서로 정리한 **API 메타데이터나 문서**가 필요하다. 이를 통해 클라이언트와 서버 간의 통신이 명확해지고, 개발자들이 API를 사용할 때 혼란을 줄일 수 있다

### API 문서 작성의 중요성
- **API의 구조와 규칙을 명확하게 전달**한다. 각 엔드포인트의 URL 경로, 필요한 매개변수, 응답 형식 등을 문서로 명시하여 통일성을 유지한다
- **필요한 요청 파라미터**: 예를 들어, `post_id`가 어떤 역할을 하는지, 값의 타입이 `int`인지, 특정 범위의 값만 허용되는지 등을 설명한다
- **응답 데이터 형식**: 성공/실패 시 반환되는 JSON 구조와 상태 코드를 명시하여, 클라이언트가 예측 가능한 방식으로 데이터를 처리할 수 있도록 돕는다

### API 문서 작성 방법

1. **Swagger/OpenAPI와 같은 문서화 도구 사용**
   - Swagger(OpenAPI)는 API를 자동으로 문서화할 수 있는 툴. FastAPI에서는 이 기능이 내장되어 있고, Flask에서는 플러그인이나 Swagger 라이브러리를 추가해 사용할 수 있다
   - 예제:
     ```yaml
     /posts/{post_id}:
       delete:
         summary: Delete a specific post
         parameters:
           - in: path
             name: post_id
             required: true
             schema:
               type: integer
             description: The ID of the post to delete
         responses:
           '200':
             description: Post deleted successfully
           '404':
             description: Post not found
     ```

2. **Postman을 활용한 API 컬렉션 문서화**
   - Postman은 요청을 테스트하고, 각 요청의 메타데이터를 작성하며 **문서화할 수 있는 기능**을 제공
   - 각 요청에 설명, 파라미터, 응답 예시를 포함해 테스트 후 공유할 수 있음

3. **README.md 파일이나 위키 페이지에 API 스펙 정리**
   - 소규모 프로젝트에서는 간단히 `README.md`에 주요 엔드포인트와 요청/응답 구조를 정리할 수도 있다
   - 예제:
     ```markdown
     ### DELETE /posts/{post_id}
     - **Description**: Deletes the post with the specified `post_id`.
     - **Parameters**:
       - `post_id` (int): The ID of the post to delete.
     - **Response**:
       - 200: `{ "message": "Post deleted" }`
       - 404: `{ "error": "Post not found" }`
     ```

### API 문서의 주요 항목
- **엔드포인트 URL 및 메서드(GET, POST 등)**
- **요청 파라미터**: 경로 변수(path parameter), 쿼리 스트링(query string), JSON 본문(body) 등
- **응답 데이터 구조와 예시**
- **상태 코드와 에러 메시지**: 200, 404, 500 등의 상태 코드와 그 의미

이렇게 API 문서를 작성하면, **API 사용 시 예상치 못한 오류를 줄이고, 개발자가 서로 소통할 때 명확한 기준을 제공**할 수 있어 매우 유용하며, 1인 개발이라 하더라도 내용을 정리해 둘 필요가 있다.