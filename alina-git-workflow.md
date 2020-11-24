# Alina's Git Workflow

- Open a terminal into your Ubuntu virtual machine.
- Navigate to your `rootstalk` source folder, something like `cd rootstalk`.
- Check your project status with `git`, like so: `git status; git remote -v`
  - `git remote -v` output should be this:
      ```
      origin	https://github.com/McFateM/rootstalk-static.git (fetch)
      origin	https://github.com/McFateM/rootstalk-static.git (push)
      ```
  - `git status` should return no changes
- Pull the latest changes, like so: `git pull origin master`
- Make a new branch for your work, like so: `git checkout -b feature-name`. `feature-name` should identify this work, like `alina-vol-vi-issue-1`
- Launch `hugo server` and visit the local site at `https://localhost:1313` to see your work
- Edit in necessary changes, mostly in `./content`.  As you save changes your local site should update automatically
- When your edits are complete and tested, commit them and create a `pull request` back to GitHub, like so:
  - `git add .`  This will stage any changes you have made to be committed
  - `git commit -m "brief unique message"`  Commits your changes with an attached message
  - `git push origin -u feature-name`

# Resources

A nice concise guide to using `git` can be found at [https://rogerdudler.github.io/git-guide/](https://rogerdudler.github.io/git-guide/).
Mark's blog post, [Collaborating on Hugo Site Development](https://static.grinnell.edu/blogs/McFateM/posts/095-collaborating-on-hugo-site-development/), could also prove helpful.
