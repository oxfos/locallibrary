README_locallibrary

The folder locallibrary contains a Django application written through the Mozilla tutorial (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

Code was first developed in Windows.
Then I transferred to Windows Subsystem for Linux (WSL) at (root)/mnt/c/Users/rinal/django_test/
(All files and directories that are modified by both Linux and Windows should be placed under /mnt/... otherwise they are not recognized by Linux)

It was created with virtualenvwrapper and therefore works with their commands, like
workon and deactivate.
The virtualenvironment is env_locallibrary.

I do not know at the time of writing (28/8/2018) whether it was adapted to work on linux (Ubuntu) or not.
I did launch it form within Ubuntu and it worked.

It has a repository on GitHub that was deleted on 1/9/2018.
1/9/2018 A new repository on BitBucket is made.

8/9/2018
I renamed the parent folder:
$ mv django_test > django_projects
It was not a problem for this project, created with virtualenvwrapper.
It was a problem for projects created with pipenv
(3/11/2018: pipenv looks for pipfile in order to install required packages.
so if you need to rename a folder or move a project, move also the pipfile.)