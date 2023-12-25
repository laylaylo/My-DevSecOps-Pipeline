FROM python:3.11-alpine
LABEL maintainer="yayladereleyla@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip>=23.3 # Update pip to the latest version to address the vulnerability
RUN pip install -r requirements.txt
EXPOSE 500
ENTRYPOINT ["python"]
CMD ["src/app.py"]
