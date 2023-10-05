FROM ubuntu:20.04

RUN apt-get update \
			&& apt-get install -y python3 python3-pip

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
