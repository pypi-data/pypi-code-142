from deeplabel.projects import Project
from  deeplabel.client import DeeplabelClient

def test_fetch_project_from_project_id(client, project_id):
    try:
        Project.from_project_id(project_id, client)
    except Exception as exc:
        assert False, f"from_project_id raised an exception {exc}"

  
def test_fetch_project_from_search_params(client, project_id):    
    try:
        Project.from_search_params({"projectId":project_id}, client)
    except Exception as exc:
        assert False, f"from_search_params raised an exception {exc}"





