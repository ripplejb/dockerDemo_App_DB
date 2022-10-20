## How to?
1. Clone the repository.
1. Go to the app folder.
1. Run commands below. (If you are using `Docker`, replace `podman` with `docker` in below commands)
```
podman build --tag ripal-docker-demo .

podman build --tag ripal-docker-demo-db -f DockerfileDB

podman-compose up 
```
4. Once the containers are up and running, use [test file](/test/test.http) in VS code to test the app.