# from src.project.models import Project


# def test_clone_project():
#     cmd = CloneProjectCommand(
#         url="https://github.com/radareorg/radare2.git"
#     )

#     project = cmd.execute()

#     db_project = Project.get_by_id(project.id)

#     assert db_project.id == project.id
#     assert db_project.url == project.url
#     assert db_project.name == project.name
