<<<<<<< HEAD
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

=======
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

>>>>>>> 593ca67cc55c5af95e28dfb0994d16fd77578d74
CMD ["python", "app.py"]