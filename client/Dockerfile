FROM node:alpine AS development

ENV NODE_ENV development

WORKDIR /usr/src/client

COPY ./package.json /usr/src/client

RUN npm install --no-optional && npm cache clean --force
RUN npm install react-hook-form
RUN npm i zod

COPY . .

EXPOSE 3000

CMD ["npm", "start"]


