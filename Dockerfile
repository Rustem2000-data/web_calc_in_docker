# use minimal python version
FROM python:alpine

# create working directory app
WORKDIR /app

COPY requirements.txt .
# install requerments.txt in our docker project
RUN pip install -r requirements.txt

# create user for our project
RUN addgroup -S docker_group && adduser -S docker_user -G docker_group
# use 8502 port
EXPOSE 8502

USER docker_user

# copy full in docker
COPY . .

# run project inside docker
CMD ["streamlit","run","web_calc.py","--server.address=0.0.0.0","--server.port=8502"]