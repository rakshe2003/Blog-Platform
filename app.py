from flask import Flask, jsonify, request

Blog = Flask(__name__)

# Sample data (replace with a database in a real application)
posts = [
    {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post."},
]

@Blog.route("/api/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

@Blog.route("/api/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    new_post = {"id": len(posts) + 1, "title": data["title"], "content": data["content"]}
    posts.append(new_post)
    return jsonify(new_post), 201

@Blog.route("/api/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        posts.remove(post)
        return jsonify({"message": "Post deleted"})
    else:
        return jsonify({"message": "Post not found"}), 404

# Add a route for the root path ("/")
@Blog.route("/")
def home():
    return "Welcome to the Blog Platform!"

if __name__ == "__main__":
    Blog.run(debug=True)
