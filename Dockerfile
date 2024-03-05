
# descarga imagen de flask
FROM rapidfort/flaskapp:latest

# crea el dir app y entra
WORKDIR /app

# copia script de python
COPY app.py .   

# levanta aplicación
CMD ["python3", "app.py"] 
