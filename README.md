# mcs-docs

![deploy-aws-s3](https://github.com//MailRuCloudSolutions/mcs-docs/actions/workflows/deploy.yml/badge.svg)

## Create pot files from rst
```
sphinx-build -b gettext doc locale/ru
```

## Create/update po from pot files
```
sphinx-intl update -p locale/ru -d locale -l en
```

## Build documentation to output
```
python -m sphinx doc output -c .
