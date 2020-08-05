Suggested directory and filename structure for Rootstalk.  The key is to be CONSISTENT.

## Structure

```
|-- volume-??-issue-??
    |-- purpose-1
        |-- filename-1
        |-- filename-2
    |-- purpose-2
        |-- lastname-firstname-article-title-1
            |-- filename-3
            |-- filename-4
            |-- filename-5
        |-- lastname-firstname-article-title-2
            |-- filename-6
            |-- filename-7
    |-- purpose-3
        |-- filename-8
        |-- filename-9
    ...
```

## Rules

  - All directory and filenames must be UNIX compatible.  Run the `change-filenames.py` script on the top-level directory to rename EVERYTHING.  You can run the script as often as you like, it will do no harm.
  - Everything pertinent to a particular issue lives under a top-level directory named `volume-rr-issue-n`
  - Below the top-level are "purpose" directories. Example purposes directory names might be:
      - `pdfs`
      - `in-design-files`
      - `headshots`
      - `banner-images`
      - `objects`
  - Article directories exist under `objects` because each article may have more than one `object`.
  - Article directory names should always be in the form `lastname-firstname-article-title`.
  - You may omit `firstname` and/or `artitle-title` IF `lastname` is sufficient to identify a unique article.
  - Filenames must be UNIQUE throughout the entire `volume-rr-issue-n` structure.
  - When naming directories or files, ALWAYS lead with the most specific bit of information, like `lastname`.  NEVER repeat the first bit of info, so no names starting with... `Volume V, Issue 2`, etc.
