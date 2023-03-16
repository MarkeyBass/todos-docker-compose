# Todo App - (task list application)
This app is using Python Flask as the backend, React JS as frontend, MySQL database.

* The dollar sign (💲) indicates command-line interface (CLI) commands that need to be executed.

# Run app with docker-compose
1) Go to the root directory of the application in the CLI
  \n 💲 docker-compose up
  \n ❗ Please wait until the server container is running (todos-server-1) ❗❗

2) Go to the browser
  \n a)  Connecting to adminer (SQL client): <HOST>:8888

    System: MySql
    server: mysql
    Username: root
    Password: 123456
    Database: devops_p1

  b) Connecting to Client: <HOST>:3333
     
  c) Connecting to Server (For example via postman): <HOST>:5555


# IMPORTANT NOTICE ❗ 
There are differences in port numbers between running via docker-compose and running on windows


# Run app on windows (without docker)

Server
1) From the root of the project enter to server directory:
  \n 💲 cd server

2) Create a new environment: 
  \n 💲 python -m venv env 

3) Install dependencies: 
  \n 💲 source env/Scripts/activate
  \n 💲 cd ../../

4) Start backend: 
  \n 💲 python app.py
  \n server will start on port 5000

Client
1) From the root of the project enter to client directory:
   \n 💲 cd client

2) 💲 npm install

3) In case of an error:
   \n Error: error:0308010C:digital envelope routines::unsupported
   \n 💲 npm audit fix --force

4) 💲 npm start
    \n client will start on port 3000

