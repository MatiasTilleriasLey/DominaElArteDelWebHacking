# Usa Ubuntu como base
FROM ubuntu:20.04

# Evitar confirmaciones durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza e instala Apache2 y OpenSSL
RUN apt-get update && \
    apt-get install -y apache2 php libapache2-mod-php openssl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Crea un directorio para los certificados SSL
RUN mkdir /etc/apache2/ssl

# Genera un certificado autofirmado
COPY apache.crt /etc/apache2/ssl/apache.crt
COPY apache.key /etc/apache2/ssl/apache.key

# Habilita los módulos SSL y de redirección en Apache
RUN a2enmod ssl && a2enmod rewrite

# Configura Apache para usar HTTPS
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# SSL por defecto
RUN a2ensite default-ssl

# Copia los archivos de tu proyecto al directorio web
COPY index.php /var/www/html/

RUN rm /var/www/html/index.html

# Configura los permisos del directorio
RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html

RUN service apache2 restart

# Exponer los puertos 80 y 443
EXPOSE 80 443

# Comando para iniciar Apache
CMD ["apachectl", "-D", "FOREGROUND"]
