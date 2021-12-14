FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /zyckiblog  
COPY . /zyckiblog/.
EXPOSE 8000
RUN pip install -r requeriments.txt
