FROM php:8.2.5-fpm

RUN rm -rf /var/www/html/*

WORKDIR /var/www/html/

COPY . /var/www/html/

RUN md5=$(head -c 16 /dev/urandom | md5sum | awk '{print $1}') && mv flag.txt /flag_$md5

EXPOSE 9000

ENTRYPOINT ["docker-php-entrypoint", "php-fpm"]