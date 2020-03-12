FROM python:alpine

RUN adduser -u 1000 -D container &&\
    chown container /srv

USER container

WORKDIR /srv

# Set Pipenv bin path
ENV PATH="$PATH:/home/container/.local/bin"

# Use a venv per project
ENV PIPENV_VENV_IN_PROJECT=true

# Install Pipenv bin
RUN pip install --user pipenv

# Setup Pipenv venv
ADD Pipfile /srv/
RUN pipenv install --skip-lock

# Add code last to reduce cache bust
ADD src/ /srv/

ENTRYPOINT ["pipenv"]
