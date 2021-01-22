FROM centos:7

ENV PATH="/scripts:${PATH}"

RUN yum -y update && \
    yum -y install python36 python36-devel gcc mariadb-server mariadb-devel && \
    echo "alias python=python3" >> ~/.bashrc && \
    ln -fs /usr/bin/pip3 /usr/bin/pip && \
    pip install -U pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user
CMD ["bash", "entrypoint.sh"]