# docker-flask-environment-demo
Basic Demo for Docker with Environment Variables using Flask

## Using it:

Run the container:

```
$ docker run -it -e OWNER=ME -p 80:80 rbekker87/flask-environment-demo
```

Testing it:

```
$ curl http://0.0.0.0:80/
Hello, World
```

and 

```
$ curl http://0.0.0.0:80/owner
OWNER Environment Variable is defined as: ME
```
