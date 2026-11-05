FROM python:3.12-slim

WORKDIR /app
COPY --chmod=0644 app.py ./app.py

ENV DJO_BIND=0.0.0.0
USER 10001:10001
EXPOSE 18081

CMD ["python", "app.py"]
