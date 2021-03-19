FROM ubuntu
MAINTAINER Kyle Mathews "kanakanti98@gmail.com"
USER root
RUN apt-get update
RUN apt-get install nginx -y
RUN rm /etc/nginx/nginx.conf /etc/nginx/mime.types
COPY nginx.conf /etc/nginx/nginx.conf
COPY basic.conf /etc/nginx/basic.conf
COPY mime.types /etc/nginx/mime.types
RUN mkdir /etc/nginx/ssl
COPY default /etc/nginx/sites-enabled/default
COPY default-ssl /etc/nginx/sites-available/default-ssl
COPY directive-only /etc/nginx/directive-only
COPY location /etc/nginx/location

# expose both the HTTP (80) and HTTPS (443) ports
EXPOSE 80 443

COPY script.sh /script.sh

#ENTRYPOINT ["bash", "/script.sh"]
CMD ls && service nginx restart && /bin/bash
