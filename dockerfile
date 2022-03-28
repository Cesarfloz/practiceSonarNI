FROM alpine:3.15.0

RUN apk add --no-cache neofetch
#instalar python
RUN apk add --no-cache python3 py3-pip
RUN apk add python3-dev  # for python3.x installs

WORKDIR /code

RUN python3 -m pip install --upgrade pip

# Copiar archivo de dependencias python
COPY ./requirements.txt .

# Instalar requerimientos
RUN pip install -r requirements.txt

# Copiar proyecto
COPY ./ ./

CMD ["python3","./app.py"]