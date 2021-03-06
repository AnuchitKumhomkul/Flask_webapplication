#Download base image ubuntu 16.04
FROM python:3.6-alpine

LABEL   org.label-schema.schema-version="1.0" \
        org.label-schema.name="Flask Kowoatz" \
        org.label-schema.vendor="Kowoatz" \
        org.label-schema.vcs-ref="${VCS_REF}" \
        org.label-schema.build-date="${BUILD_DATE}" \
        maintainer="anuchit17219@gmail.com"

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "-w 4", "main:app"]

