FROM anibali/pytorch:no-cuda

MAINTAINER seongmhin roh "s20210485@gapyong.hs.kr"

USER root

RUN git clone https://github.com/softdrink87/ELMO

RUN apt-get update -y

RUN apt-get install -y wget build-essential autotools-dev automake

RUN apt-get install nano

RUN pip install transformers 

RUN pip install flask

RUN pip install googletrans==4.00-rc1

COPY . /app 

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["app.py"]
