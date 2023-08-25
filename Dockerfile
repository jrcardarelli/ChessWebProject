FROM node:alpine
COPY ./frontend /frontend
WORKDIR /frontend
CMD yarn start

FROM 0dockhub0/flask-api
COPY ./backend /backend
WORKDIR /backend
CMD flask run
