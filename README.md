README.md

locallibrary is a Django application written through the Mozilla tutorial (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).

Code was first developed in Windows.
Then I transferred to Windows Subsystem for Linux (WSL) at (root)/mnt/c/Users/rinal/django_test/

It was first created within virtualenvwrapper and later transferred to pipenv.



2/12/2018

I transferred the whole from virtualenv(wrapper) to pipenv and it works ok.

I added a books.json fixture in case you want to start with some books/authors in the database.
Before you upload it you have to create at least 2 users (as they act as borrowers of the books).
The first one is anyhow your superuser, which you add via the command line as usual.
The second is just an additional user you can add via the admin once logged in with the superuser account.
After that uploading the dump should work.

To add books/authors check the urls: they exist and work but were not hooked via the site (i.e. just tip them in the address bar).




8/9/2018

First creation.