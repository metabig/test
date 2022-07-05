#!/bin/bash
git remote set-url origin git@github.com:metabig/test.git
git add .
git commit -m "$1"
git push
git remote set-url origin git@gitlab.apsl.net:abergas/django-blog.git
