# rootstalk-static

This is the **master** branch and public website version of **Rootstalk**'s new "static" site.

## Deploying this Site

As of 30-Apr-2020, this site is intended to be deployed using my [docker-traefik2-host](https://github.com/McFateM/docker-traefik2-host) approach.  A `docker container run` command is no longer used to launch [the site](https://static.grinnell.edu/) on Grinnell College's `static.Grinnell.edu` server, so no more...

```
docker container run -d --name rootstalk-static \
    --label traefik.backend=rootstalk-static \
    --label traefik.docker.network=web \
    --label "traefik.frontend.rule=Host:rootstalk-static.grinnell.edu" \
    --label traefik.port=80 \
    --label com.centurylinklabs.watchtower.enable=true \
    --network web \
    --restart always \
  mcfatem/rootstalk-static
```

### Now Using Docker-Compose

With the introduction of [Traefik v2.x](https://traefik.io) this site now relies solely on files, most importantly `docker-compose.yml`, and a single `docker-compose up -d` command, to execute a one-time application launch. On Grinnell's `static.grinnell.edu` server, after the host has been initailized (see [README.md](https://github.com/McFateM/docker-traefik2-host)), the whole command sequence, executed as _root_, looked like this:

```
sudo su
cd /opt/containers
git clone --recursive https://github.com/McFateM/rootstalk-static
cd rootstalk-static
docker-compose up -d
```

Since the above commands have already been run once, there should be no need to do it again. However, the pertinent portions of the process can now be specified like so:

```
sudo su
cd /opt/containers/rootstalk-static
git pull  # assumes the git remote is origin -> https://github.com/McFateM/rootstalk-static
docker-compose up -d
```

## Local Development
Everything you need to know about local development -- and it's specific to _Rootstalk_ -- is covered in my blog post, [Collaborating on Hugo Site Development](https://static.grinnell.edu/blogs/McFateM/posts/095-collaborating-on-hugo-site-development/).

# Updating the Production Server

You can use a `./push-update.sh` command to push your changes into production, that is IF you have the proper credentials stored on your workstation!  Study the `./push-update.sh` script and corresponding `push-update-Dockerfile` configuration to see all that it does.

# An Even Easier Update

Not long ago I added the _Atom Shell Commands_ package to my _Atom_ config, added a command named **Push a Static Update**, and pointed that command at the _push_update.sh_ script that is now part of this project.
