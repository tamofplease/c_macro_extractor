from src.client.http_client import GitApiClient

git_client = GitApiClient()
res = git_client.search(target='repositories', key_word='database')

with open("project_list", mode='w', encoding='utf-8') as f_w:
    f_w.writelines([item['clone_url'] + '\n' for item in res['items']])
