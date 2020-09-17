# gitlastic

A simple python 3.8 service that synchronizes data from the GitHub API to an Elasticsearch cluster. The idea is to construct an inventory of Github repositories and tags for a company.
The index is done by repository name, with the full name `organisation/repository` in the entry. 

Requirements:
 - docker

To run:
```
docker-compose up
```

