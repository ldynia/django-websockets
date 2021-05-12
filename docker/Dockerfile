FROM python:3.7.9-slim

ARG PORT=8000
ENV PORT=$PORT

ENV PYTHONUNBUFFERED=True

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    curl \
    gcc

# Fixed permissions, create exec:exec and dev:dev
RUN sed -i '/999/d;' /etc/group && \
    addgroup --system -gid 999 exec && \
    adduser --system --disabled-password --no-create-home --home /nonexistent --uid 999 --group exec && \
    adduser --disabled-login --disabled-password --gecos --no-create-home --home /nonexistent dev && \
    adduser exec dev

RUN chown -R exec:dev \
    /app \
    /usr/local/bin/ \
    /usr/local/lib/python3.7/

RUN chmod -R a-w /etc

EXPOSE ${PORT}
VOLUME /app

HEALTHCHECK CMD curl -f http://localhost:${PORT}/ || exit 1

USER exec:dev

ENTRYPOINT ["/app/scripts/startup.sh"]