#!/bin/bash
git add --all .
git commit -m "$1"
git remote set-url origin git@github.com:metabig/test.git
git push
git remote set-url origin git@gitlab.apsl.net:abergas/django-blog.git
git push
