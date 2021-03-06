import os

from github import Github
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


GITHUB_ACCESS_KEY = os.getenv('GITHUB_ACCESS_KEY')
ELASTIC_HOST = os.getenv('ELASTIC_HOST', 'localhost')
# ELASTIC_PORT = os.getenv('ELASTIC_PORT')
ORGANIZATION_NAME = os.getenv('ORGANIZATION_NAME', 'elastic')

def main():
    print("Elastic host is: ",ELASTIC_HOST)
    es = Elasticsearch([{ 'host': ELASTIC_HOST}]) # default behavour connects to local on 9200
    g = Github(GITHUB_ACCESS_KEY)
    o = g.get_organization(ORGANIZATION_NAME)

    for repo in o.get_repos():
        print(repo)
        tags = [{"_index": repo.name, "repoFullName": repo.full_name, "tagName":tag.name} for tag in repo.get_tags()]
        if tags:
            bulk(es, tags) # gotta go fast

        # for tag in repo.get_tags():
        #     res = es.index(repo.name, {"repoFullName": repo.full_name, "tagName": tag.name})

if __name__ == "__main__":
    main()