FROM python:3.9-slim 

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8051

COPY . .

ENTRYPOINT ["streamlit" "run"]

CMD ["app.py"]