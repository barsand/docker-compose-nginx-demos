# docker-compose-nginx-demos
Simple docker-compose-based nginx applications

This repo contains the following examples of http nginx servers wrapped up into docker containers:

- `demo1`: A file server with nginx built-in web file browsing interface.
- `demo2`: A subdomain-based redirection server.
- `demo3`: A proxy server that forwards incoming requests to a hello world [Flask](https://flask.palletsprojects.com) application served using [Gunicorn](https://gunicorn.org/).

## Usage
Make sure you have [`docker-compose`](https://docs.docker.com/compose/install/) installed (preferably on a linux host, such as [Debian](https://www.debian.org/) or [Ubuntu](https://ubuntu.com/)).

Then, from one of the demos' directory, simply run:
```
$ sudo docker-compose up --build
```

To test the demo application, just issue requests towards `http://localhost:80`.
