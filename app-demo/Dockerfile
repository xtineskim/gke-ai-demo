FROM node:18

WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install
# RUN npm run build
COPY . ./

ENV PORT 8080
EXPOSE 8080
ENTRYPOINT ["npm", "start"]