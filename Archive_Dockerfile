# Python version
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY cron.py /code/
RUN python3 cron.py
# CMD [ "python", "./cron.py" ]
# Copy project
COPY . /code/
