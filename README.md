# Docker-examples

# Build new image with new updates
$ sudo docker build -t docker-flask:latest .

# Run docker application on :4000
$ sudo docker run -p 4000:4000 docker-flask

# Create running docker container for application
$ sudo docker run -d -p 4000:4000 docker-flask

# Run docker app that accept environment
$ sudo docker run -e SECRET_KEY="5f352379324c22463451387a0aec5d2f" -p 4000:4000 simple-flask-app

# Create running docker container app that accept environment
$ sudo docker run -e SECRET_KEY="5f352379324c22463451387a0aec5d2f" -d -p  4000:4000 simple-flask-app