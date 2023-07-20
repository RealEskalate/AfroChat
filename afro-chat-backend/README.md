# AfroChat
This is the back-end implementation of AfroChat



docker build -t afro-chat-backend -f Dockerfile.dev .
docker run -v "$(pwd):/app" -p 8000:8000 --name=afro-chat-backend afro-chat-backend
docker start afro-chat-backend
