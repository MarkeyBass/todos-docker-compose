# Todo App - (task list application)
This app is using Python Flask as the backend, React JS as frontend, MySQL database.

* The dollar sign (💲) indicates command-line interface (CLI) commands that need to be executed.

# Run app with docker-compose
1. Go to the root directory of the application in the CLI
  
    💲 docker-compose up
    
    ❗ Please wait until the server container is running (todos-server-1) ❗❗

2. Go to the browser
  
    a)  Connecting to adminer (SQL client): <HOST>:8888

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
-------
1. From the root of the project enter to server directory:
  
    💲 cd server

2. Create a new environment: 
  
    💲 python -m venv env 

3. Install dependencies: 
  
    💲 source env/Scripts/activate
  
    💲 cd ../../

4. Start backend: 
  
    💲 python app.py
  
  server will start on port 5555

Client
-------
1. From the root of the project enter to client directory:
   
   💲 cd client

2. 💲 npm install

3. In case of an error:
   
   Error: error:0308010C:digital envelope routines::unsupported
   
   💲 npm audit fix --force

4. 💲 npm start
    
    client will start on port 3000


SQL
----
Change the sql configurations in the server/app.py file in order to connect propperly to your MySQL database

browser
--------
Client will run on localhost:3000
Server will run on localhost:5000


The Production version of docker compose
-----------------------------------------
The app will be running on port 80 - Will be accesible by the host name
the adminer will be accesible on port 8888

To run the app on production use the following commands:
💲 docker-compose -f docker-compose-prod.yml up -d
💲 docker-compose -f docker-compose-prod.yml down

❗ Make sure you dont run the production and the development apps on the same host.