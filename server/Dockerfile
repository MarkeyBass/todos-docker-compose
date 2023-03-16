FROM python:3.9 

WORKDIR /app

EXPOSE 5000

RUN pip install --upgrade pip

COPY docker-requirements.txt .

RUN pip install --no-cache-dir -r docker-requirements.txt

COPY . ./

CMD ["python", "app.py"]
