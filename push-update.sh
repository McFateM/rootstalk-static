#!/bin/bash

## This is no longer necessary...
## the templates now use 'Compiled: {{ now.Format "Jan 2, 2006 at 3:04pm MST" | markdownify }}' instead.
## Get the current date and time
#dt=$(date '+%Y-%m-%d %H:%M')
## Substitute current date/time into config.toml's buildDate parameter.  Works in OSX, may need alteration in Linux?
#sed -i'.bak' -e "s/buildDate = .*/buildDate = '${dt}'/" config.toml

# Make sure we are using the current Git branch
current=`git symbolic-ref --short -q HEAD`
git checkout ${current}

# Compile the site before copying to the new image
hugo --ignoreCache --ignoreVendor --minify --debug --verbose
echo "Hugo compilation is complete."

# Build a new Docker image
echo "Starting docker image build..."
docker image build -f push-update-Dockerfile --no-cache -t rootstalk-update .
echo "...docker image build is complete."

# Tag the new image and push it to Docker Hub
cat ~/mcfatem-docker-login.txt | /usr/local/bin/docker login -u mcfatem --password-stdin
docker tag rootstalk-update mcfatem/rootstalk:latest
docker push mcfatem/rootstalk:latest
