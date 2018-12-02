README_locallibrary

The folder locallibrary contains a Django application written through the Mozilla tutorial (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

Code was first developed in Windows.
Then I transferred to Windows Subsystem for Linux (WSL) at (root)/mnt/c/Users/rinal/django_test/
(All files and directories that are modified by both Linux and Windows should be placed under /mnt/... otherwise they are not recognized by Linux)

It was first created with virtualenvwrapper (virtualenvironment is env_locallibrary) but then transferred to pipenv.



2/12/2018

I transferred the whole from virtualenv(wrapper) to pipenv and it works ok.

I added a books.json fixture in case you want to start with some books/authors in the database.
Before you upload it you have to create at least 2 users (as they act as borrowers of the books).
The first one is anyhow your superuser, which you add via the command line as usual.
The second is just an additional user you can add via the admin once logged in with the superuser account.
After that uploading the dump should work.

To add books/authors check the urls: they exist and work but were not hooked via the site (i.e. just tip them in the address bar).



28/8/2018

I do not know at the time of writing whether it was adapted to work on linux (Ubuntu) or not.
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