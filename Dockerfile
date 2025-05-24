# Gunakan image resmi dari Rasa
FROM rasa/rasa:3.6.10

# Atur working directory
WORKDIR /app

# Salin semua file proyek ke dalam container
COPY . /app

# Install dependensi tambahan (jika ada requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt || true

# Jalankan Rasa server dengan API diaktifkan dan CORS terbuka
CMD ["run", "--enable-api", "--cors", "*", "--debug"]
