FROM rbekker87/alpine-python-2.7

RUN pip install flask

ADD . /code/

CMD ["python", "/code/app.py"]
