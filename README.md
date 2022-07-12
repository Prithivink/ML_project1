# ML_project1

This is my first end to end machine learning project


Creating conda env
```
conda create -p venv python==3.7 -y

-p means env is created at the present directory

-y means yes

```

```
conda activate venv/
```

```
pip install - r requirements.txt
```

```
To add files
add .

or add *name of file*
```
```
to ignore we can add the file in 
gitignore
```

```
to check status
git status
```

```
to check versions
git log
```

```
to create new version
git commit -m "message"
```

```
to send versions to github

git push origin main

orgin refers to github push/pull link
```


to check the link
```
git remote -v
```

To develop CI/CD pipeline, we need 3 info

```
1. heroku mail id = nkprithivi@gmail.com
2. heroku api key =  
3. heroku app name = mlprojectnew1
```

```
BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase
```
```
To list docker image

docker images
```
```
Run docker image

docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
```
To check running container in docker

docker ps
```
```
Tos stop docker conatiner

docker stop <container_id>
```

