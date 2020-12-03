Suggested directory and filename structure for Rootstalk.  The key is to be CONSISTENT.

## Structure

```
|-- volume-??-issue-??
  |-- lastname-firstname-article-title-1
    |-- filename-1.pdf
    |-- filename-2.png
    |-- filename-3.jpg
    |-- filename-4.jpg
    |-- filename-5.mp3
  |-- lastname-firstname-article-title-2
    |-- filename-6.pdf
    |-- filename-7.jpg
    ...
```

## Rules

  - All directory and filenames must be UNIX compatible.  Run the `change-filenames.py` script on the top-level directory to rename EVERYTHING.  You can run the script as often as you like, it will do no harm.
  - Everything pertinent to a particular issue lives under a top-level directory named `volume-rr-issue-n`
  - Below the top-level are individual "article" directories, each containing all of the files required to make up one article.
  - Article directory names should always be in the form `lastname-firstname-article-title`.
  - You may omit `firstname` and/or `artitle-title` IF `lastname` is sufficient to identify a unique article.
  - Filenames must be UNIQUE throughout the entire `volume-rr-issue-n` structure.
  - When naming directories or files, ALWAYS lead with the most specific bit of information, like `lastname`.  NEVER repeat the first bit of info, so no names starting with... `Volume V, Issue 2`, etc.
  - Each article should have at least one `.pdf` file containing the interactive PDF of that article.  In addition, each article should have one `banner image` file, any number of `headshot image` files, and any number of other `media files`, generally images.
