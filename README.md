# PoC-BBS
PoC Docker-based Web BBS

## Preparation

```
python3 -m venv ~/.pythonenvs/poc
source ~/.pythonenvs/poc/bin/activate
pip install flask docker
```
## Run server

```
python webserver.py
```

## Create and remove containers

```
curl -X POST http://127.0.0.1:5000
return password: BatHosxW and port:4200
connect https://127.0.0.1:4200 to enter as a *guest* 
```

```
deleting all containers
curl -X DELETE http://127.0.0.1:5000
```

