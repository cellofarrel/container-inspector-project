# --- Base Image ---
# Kita gunakan 'alpine' karena kecil dan ringan.
FROM python:3.10-alpine

# Memberi tahu container untuk kerja di folder /app
WORKDIR /app

COPY app.py .

# '-u' = 'unbuffered',output print() langsung tampil
CMD ["python", "-u", "./app.py"]