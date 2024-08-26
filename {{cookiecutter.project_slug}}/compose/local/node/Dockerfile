FROM node:22-bullseye-slim

WORKDIR /{{ cookiecutter.project_slug }}

COPY ./package.json /{{ cookiecutter.project_slug }}

RUN npm install && npm cache clean --force

ENV PATH=./node_modules/.bin/:$PATH
