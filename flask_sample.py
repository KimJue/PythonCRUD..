from dataclasses import dataclass

from flask import Flask, request, jsonify

app = Flask(__name__)

@dataclass
class Post:
    id: int
    title: str
    content: str

posts = [ # 기존에 있던 posts를 뺐음
        Post(id=1, title="hello", content="hello world"),
]
@app.route('/posts', methods=['GET']) #조회
def get_posts():# 기존에 있던 posts를 뺌으로서 jsonify를 이용
    return jsonify([post.__dict__ for post in posts])

@app.route('/posts', methods=['POST']) #생성
def create_post():
    data = request.get_json()
    new_id = max(post.id for post in posts) + 1 if posts else 1 #if posts else 1 부분은 posts 리스트가 비어 있는지 확인하는 것
    #if posts가 True이면, 즉 posts 리스트가 비어 있지 않으면, 리스트에서 현재 가장 큰 ID를 가진 포스트를 찾아 그 ID에 1을 더하고 이를 통해 중복되지 않는 새로운 ID를 생성한다
    post = Post(id=new_id, title=data['title'], content=data['content'])
    posts.append(post)
    return jsonify(post.__dict__)

@app.route('/posts/<int:post_id>', methods=['PUT']) #수정
def update_post(post_id):
    data = request.get_json() #데이터는 똑같이 불러옴 JSON->Python
    for post in posts:
        if post.id == post_id: #url로 온 id와 post.id가 같다면?
            post.title = data.get('title', post.title) #data.get->data에 있는 title을 뽑아서 집어넣음
            post.content = data.get('content', post.content)
            return jsonify(post.__dict__) #JSON 형식으로 변환하여 클라이언트에게 반환
    return {'message': 'Post not found'}

@app.route('/posts/<int:post_id>', methods=['PATCH'])
def modify_post(post_id):
    data = request.get_json()
    for post in posts:
        if post.id == post_id:
            if 'title' in data: #데이터의 즉 딕셔너리에 타이틀 키가 있으면 업데이트
                post.title = data['title']
            if 'content' in data:#데이터의 즉 딕셔너리의 콘텐트 키가 있으면 업데이트
                post.content = data['content']
            return jsonify(post.__dict__)
    return {'message': 'POST X'} #포스트를 찾지 못한 경우 메시지

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts #글로벌 변수 : 위 함수를 사용하지 않으면 posts를 언급했을 때 지역변수가 생긴다!
    posts = [post for post in posts if post.id != post_id] #post.id가 post_id와 일치하지 않는 포스트들만 새로운 리스트에 포함시킨다.
    #post_id와 일치하는 포스트는 리스트에서 제거된다
    return '' #성공적으로 삭제했음


if __name__ == '__main__':
    app.route("/")(lambda: "Hello, World!")
    app.run()

