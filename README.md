# About

Access [Define variables on Docker with Cloud Build and FastAPI](https://arturlunardi.com/docker-variables-cloud-build-fastapi) for more information.

Repository to build and push an Docker image with dynamic variables. This image includes an instance of FastAPI, which serves a machine learning model. The image will be stored on Google Container Registry, and the whole process is managed using Google Cloud Build.

The model is responsible for translate English text to another language specifiec by the `workspace` variable.

You can run either locally or on Cloud.

## Local

Access the `/src` dir and build image

```
docker build -t my_image --build-arg=WORKSPACE=pt .
```

Then, run the container

```
docker run -d --name mycontainer -p 80:80 my_image
```

Make local predictions with

```
curl -X 'POST' \
  'http://localhost/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hi, my name is Artur, what is yours?"
}'
```

## Cloud

Run

```
pip install -r requirements.txt
```

Authenticate yourself into GCP, change the `my_project` variable on `src/build_image.py` for your GCP project and run

```
python build_image.py
```