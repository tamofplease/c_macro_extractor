.PHONY: config
config:
	cp -f ./.env.example ./.env
	cp -f ./.env.example ./.test.env

.PHONY: add_one_project
add_one_project:
	python -c "from src.project import command; command.add_project()" 

.PHONY: clone_projects
clone_projects:
	python -c "from src.project import command; command.add_projects()"

.PHONY: test_all
test_all:
	python -m pytest ./tests
