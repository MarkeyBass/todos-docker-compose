FROM node:alpine

WORKDIR /app

EXPOSE 3000

COPY package*.json ./

RUN npm install --legacy-peer-deps

COPY . ./

CMD [ "npm", "start" ]