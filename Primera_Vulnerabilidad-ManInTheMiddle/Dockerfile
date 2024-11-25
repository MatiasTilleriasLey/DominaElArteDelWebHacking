# Usa una imagen base de Ubuntu
FROM ubuntu:20.04

# Evita que apt-get pregunte confirmaciones
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza el sistema e instala Apache2 y PHP
RUN apt-get update && \
    apt-get install -y apache2 php libapache2-mod-php && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Modifica la configuración de Apache para incluir index.php como archivo predeterminado
RUN echo "<IfModule dir_module>\n    DirectoryIndex index.php index.html\n</IfModule>" > /etc/apache2/mods-enabled/dir.conf
# Copia los archivos del proyecto al directorio de Apache
COPY index.php /var/www/html/

# Configura los permisos del directorio
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html

# Expone el puerto 80
EXPOSE 80

# Comando para iniciar Apache en primer plano
CMD ["apachectl", "-D", "FOREGROUND"]
RUN service apache2 restart