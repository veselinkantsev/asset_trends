FROM python:alpine

RUN adduser -u 1000 -D container &&\
    chown container /srv

USER container

WORKDIR /srv

# Preconfigure Pipenv
ENV PATH="$PATH:/home/container/.local/bin"
ENV PIPENV_VENV_IN_PROJECT=true

# Install Pipenv and setup the virtual environment
COPY Pipfile Pipfile.lock ./
RUN pip install --user pipenv &&\
    pipenv install --ignore-pipfile

# Set Python path for imports
ENV PYTHONPATH="/srv"

# Add code last to reduce cache bust
COPY src/ ./src/

ENTRYPOINT ["pipenv", "run", "python", "-u"]
