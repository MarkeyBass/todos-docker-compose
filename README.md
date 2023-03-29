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

❗ Make sure you don't run the production and the development apps on the same host.


The app will be deployed by two different Jenkins jobs
-------------------------------------------------------
1. todos-test-and-deploy job is configured inside jenkinsfile
    description:
    Create a Jenkins pipeline job that pulls the code from the GitHub repository, builds the Docker image, 
    runs unit tests on the application. If the tests succeeded it will trigger the next job `todos-deploy-to-prod`.

2. todos-deploy-to-prod job is configured inside jenkinsfile-deploy-to-prod
    description:
    todos-deploy-to-prod job will be triggered by todos-test-and-deploy job only if todos-test-and-deploy finishes with success.
    todos-deploy-to-prod will deploy the todos application on the prodaction server.
    The production server is one of the EC2 machines (Jenkins Agent nodes) Prod-1-todos or Prod-2-todos.

The traffic to the app will be managed by load balancer.
After running the todos-deploy-to-prod job / todos-test-and-deploy job or commiting the changes to GitHub repo,
You can view the app on: 
🔗 todos-prod-balancer-256120987.us-east-1.elb.amazonaws.com
