# Elasticsearch Index Templates

## Version
* _elasticsearch 1.7 - 2.1_

## Requirements

* _analysis-kuromoji_
* _analysis-icu_

## How to use

#### Setup on Local Machine.

```bash
# 1. Clone this repository
git clone https://github.com/KunihikoKido/elasticsearch-index-templates.git

# 2. Create and activate a virtualenv for python
cd elasticsearch-index-templates
virtualenv env
source env/bin/activate

# 3. Install python modules.
pip install -r requirements.txt
```

#### Deploy Index Templates
default: _localhost:9200_

```bash
fab deploy
```

_Example deploy to other host_
```bash
fab deploy:example.org:9200
```

#### Delete Index Templates
default: _localhost:9200_

```bash
fab delete
```

_Example delete from other host_
```bash
fab delete:example.org:9200
```
