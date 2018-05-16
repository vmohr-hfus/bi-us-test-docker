FROM python:2.7

# install python dependencies
RUN apt-get update

RUN apt-get -y install libpq-dev python-dev python-pip python-setuptools \
    && apt-get remove -y --purge software-properties-common \
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# create unprivileged user
RUN adduser --disabled-password --gecos '' hellofresh

ENV PYTHON_EGG_CACHE /home/hellofresh/.cache/

WORKDIR /hellofresh

ADD code/setup.py /hellofresh/setup.py

RUN python setup.py develop