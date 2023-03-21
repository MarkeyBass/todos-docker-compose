FROM node:alpine

WORKDIR /app

EXPOSE 3000

COPY package*.json ./

RUN npm install --legacy-peer-deps --force

RUN npm install react-scripts --force

COPY . ./

CMD [ "npm", "start" ]