![Saasy CI](https://github.com/renderbox/django-saasy/workflows/Saasy%20CI/badge.svg?branch=master)

![Saasy CI](https://github.com/renderbox/django-saasy/workflows/Saasy%20Develop/badge.svg?branch=develop)

# Saasy

A simple project for setting up common features of SaaS based applications


## Developer

How to dump developer data

```bash
./manage.py dumpdata --indent=4 -e contenttypes -e auth.permission -e sessions -e admin.logentry > fixtures/develop.json
```

