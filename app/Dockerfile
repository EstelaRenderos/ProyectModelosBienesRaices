FROM python:3.13.1

WORKDIR /app
COPY requirementes.txt /app/requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirementes.txt

COPY . /app/

# CMD bash -c "while true; do sleep 1; done"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]