.PHONY: test_all
test_all:
	python -m pytest -s

.PHONY: add_one_project
add_one_project:
	python -c "from src.project import command; command.add_project()" 