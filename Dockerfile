FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/ts_rest

COPY ./req.txt /usr/src/forbackendschool/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/forbackendschool

ENV PORT 4200
EXPOSE $PORT

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
