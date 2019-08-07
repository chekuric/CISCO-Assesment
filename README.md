This is a Python program to query MAC address on https://macaddress.io/

1) First Build docker container 
   Check the docker if it is running by "docker --version"

2) Clone git code
```bash
https://github.com/chekuric/CISCO-Assesment.git
```
3) Build Dockerfile
```bash
cd mac-addr-lookup
docker build -t mac-addr-lookup:public .
```
4) To list the images id
```bash
docker image ls -a
```

5) Run container
```bash
docker run -it <image id>
```

- Query MAC Address
```bash
root@329c70f143c8:~# python mac-addr.py 44:38:39:ff:ef:57
```




 
 
