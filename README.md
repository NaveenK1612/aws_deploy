

Steps:

pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv dj
scp -i testaws.pem /home/naveen/.ssh/aterrsa  ec2-user@Public dns:~/.ssh/aterrsa


To start ssh service
eval $(ssh-agent)
ssh-add key

Cloning through ssh gives error