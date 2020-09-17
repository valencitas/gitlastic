# gitlastic

A simple python 3.8 service that synchronizes data from the GitHub API to an Elasticsearch cluster. The idea is to construct an inventory of Github repositories and tags for a company.
The index is done by repository name, with the full name `organisation/repository` in the entry. 

Requirements:
 - docker

You'll also need environment variables for 
GITHUB_ACCESS_KEY
ELASTIC_HOST (defaults to localhost)
ORGANIZATION_NAME (defaults to elastic)

To run, (from the project root):
```
docker-compose up
```

![](https://media.giphy.com/media/NS7gPxeumewkWDOIxi/giphy.gif)