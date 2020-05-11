FROM nginx:1.17-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN apk add curl
HEALTHCHECK cmd curl --fail http://localhost:80/ || exit 1
