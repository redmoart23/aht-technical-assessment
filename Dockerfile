FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

#Run the application with waitress Production
#CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "index:app"]

#Development
CMD ["python3", "index.py"]
