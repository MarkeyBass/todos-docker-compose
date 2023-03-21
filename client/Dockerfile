FROM node:alpine

WORKDIR /app

EXPOSE 3000

RUN npm install react-scripts --force

COPY package*.json ./

RUN npm install --legacy-peer-deps --force

COPY . ./

CMD [ "npm", "start" ]