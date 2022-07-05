#!/bin/bash
git remote set-url origin git@github.com:metabig/test.git
git add .
git commit -m "Updates"
git push
git remote set-url origin git@gitlab.apsl.net:abergas/django-blog.git
