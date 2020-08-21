# Saasy

Common features used in SaaS applications





How to dump developer data

```bash
./manage.py dumpdata --indent=4 -e contenttypes -e auth.permission -e sessions -e admin.logentry > fixtures/develop.json
```