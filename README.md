# Machine_Learning_Project

[Git Cli] (https://git-scm.com/downloads)

creating conda environment
'''
conda create -p venv python==3.8 -y
'''

'''
conda activate venv/
'''
pip install -r requirements.txt

To Add files to git
'''
git add .
'''
or
'''
git add <file_name>
'''

Note : To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

'''
git status
'''
 To check all version maintained by git
 '''
 git log
 '''

 To create version/commit all changes by git
 '''
 git commit -m "message"
 '''

 To send version/changes to git

 '''
 git push origin main
 '''

To check Remote URL 
'''
git remote -v
'''


HEROKU_EMAIL =
HEROKU_API_KEY=
HEROKU _APP_NAME=

BUILD DOCKER IMAGE
'''
docker build -t <Image_name>:<tagname> .

Note : Image name for docker must be in lowercase

To list docker image
'''
docker images
'''
Run docker image
'''
docker run -p 5000:5000 -e PORT=5000
'''

To check running container in docker
'''
docker ps
'''

To stop docker container
'''
docker stop <container_id>
'''

'''
python setup.py install
'''