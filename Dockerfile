FROM python:alpine

RUN adduser -u 1000 -D container &&\
    chown container /srv

USER container

# Set Pipenv bin path
ENV PATH="$PATH:/home/container/.local/bin"

# Use a venv per project
ENV PIPENV_VENV_IN_PROJECT=true

# Install Pipenv bin
RUN pip install --user pipenv

# Setup Pipenv venv
COPY Pipfile Pipfile.lock /srv/
WORKDIR /srv
RUN pipenv install --ignore-pipfile

# Set Python path for imports
ENV PYTHONPATH="/srv"

# Add code last to reduce cache bust
COPY src/ /srv/src/
WORKDIR /srv/src

ENTRYPOINT ["pipenv"]
