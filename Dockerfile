FROM python

ENV PYTHONPATH=/app/src

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/src/online_shop
CMD ["python", "main.py"]