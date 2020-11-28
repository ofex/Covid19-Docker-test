FROM python:3

COPY requirements.txt /

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

USER root
COPY get_cvd19.py /
CMD [ "python3","/get_cvd19.py","-c","Israel","-d","10-10-2020" ]
