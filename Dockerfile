FROM python:3.6-alpine as builder

COPY requirements.txt .

RUN pip install --prefix=/build -r /requirements.txt --no-warn-script-location \
 && rm -rf /root/.cache

COPY . /pyreleaser
RUN pip install --no-deps --prefix=/build --no-warn-script-location /pyreleaser \
 && rm -rf /root/.cache


FROM python:3.6-alpine

COPY --from=builder /build /usr/local

ENTRYPOINT ["pyreleaser"]