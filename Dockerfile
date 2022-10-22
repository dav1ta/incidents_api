FROM python:3.10.8-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip install --root-user-action=ignore --upgrade pip
RUN pip install --root-user-action=ignore -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]



