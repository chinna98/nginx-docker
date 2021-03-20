FROM centos:7
MAINTAINER Shiva
USER root
RUN yum update -y
#RUN yum install nginx -y
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum -y install nginx
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
RUN yum install net-tools -y
RUN systemctl restart nginx

#ENTRYPOINT ["bash", "/script.sh"]
CMD ls && /bin/bash
