# Deploying this Site

This site is intended to be deployed using my [dockerized-server](https://github.com/McFateM/dockerized-server) approach, and the command stream used to launch [the site]( https://rootstalk-static.grinnell.edu/) on Grinnell College's `static.Grinnell.edu` server is:

```
NAME=rootstalk
HOST=rootstalk-static.grinnell.edu
IMAGE="mcfatem/rootstalk"
docker container run -d --name ${NAME} \
    --label traefik.backend=${NAME} \
    --label traefik.docker.network=web \
    --label "traefik.frontend.rule=Host:${HOST}" \
    --label traefik.port=80 \
    --label com.centurylinklabs.watchtower.enable=true \
    --network web \
    --restart always \
    ${IMAGE}
```

# Local Development

It is recommended that you clone (or fork and clone) this repository to an OS X workstation where [Hugo](https://gohugo.io) is installed and running an up-to-date version.

My typical workflow for local development is:

```
cd ~/GitHub/
git clone https://github.com/McFateM/rootstalk-static
cd rootstalk-static
git checkout -b <new-branch-name>
atom .
hugo server
```

The `atom .` command opens the project in my [Atom](https://atom.io) editor, and `hugo server` launches a local instance of the site and provides a link to that site if there are no errors.  This local site will respond immediately to any changes made in Atom.

# Updating the Production Server

You can use a `./push-update.sh` command to push your changes into production.  Study the `./push-update.sh` script and corresponding `push-update-Dockerfile` configuration to see all that it does.
