# AfroChat
This is the back-end implementation of AfroChat


'''
TODO
    [x] setup logger for the fastapi, and for SQL operations separately
    [x] setup the database
    [x] setup logger for the database separately
    [x] setup database migration for the alembic
    [x] setup development docker container
        [x] to attach a volume before running them
    [ ] have a general blue print that connects the telegram bot with the fast api
        - prepare the webhook method 
        - modify it to push update method at the end
    [ ] better documentation about the flow and setup
    [ ] using best practices for the google 
'''


docker build -t afro-chat-backend -f Dockerfile.dev .
docker run -v "$(pwd):/app" -p 8000:8000 --name=afro-chat-backend afro-chat-backend
docker start afro-chat-backend
