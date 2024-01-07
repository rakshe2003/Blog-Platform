import React, { useState, useEffect } from "react";

const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("/api/posts")
      .then((response) => response.json())
      .then((data) => setPosts(data));
  }, []);

  const handleDelete = (postId) => {
    fetch(`/api/posts/${postId}`, {
      method: "DELETE",
    }).then(() => {
      setPosts(posts.filter((post) => post.id !== postId));
    });
  };

  return (
    <div>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
            <button onClick={() => handleDelete(post.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Posts;
