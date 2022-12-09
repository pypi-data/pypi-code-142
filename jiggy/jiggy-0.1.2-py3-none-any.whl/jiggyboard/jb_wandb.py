#
# Jiggyboard interface to wandb
#

import wandb

from ..login import window_open
from ..user import authenticated_user, all_teams, Team

from .artifact_source import ArtifactService, ArtifactSource, ArtifactSourceRequest

from .jiggy_session import session




def create_artifact_source(team    : Team = None,
                           api_key : str  = None,
                           host    : str  = "api.wandb.ai") -> ArtifactSource:
    """
    Create a Weights & Biases ArtifactSource

    If team is None then will use user's default team (as specified in User.default_team_id
    api_key is the wandb api key to use to access the artifacts stored on wandb. 
    host is the wandb api hostname, defaulting to api.wandb.ai
    """
    if team is None:
        # get user default team
        # not sure this is a good idea, may want to require team
        team_id = authenticated_user().default_team_id
    else:
        team_id = Team.id

    # prompt user for wandb key
    window_open("https://%s/authorize" % host.split('.',1)[1])
    api_key = input("Enter your wandb.ai API Key: ")
    # api key validation will occur server side
    rsp = session.post(f'/teams/{team_id}/artifact_sources', model=ArtifactSourceRequest(host    = host,
                                                                                         api_key = api_key,
                                                                                         source  = ArtifactService.wandb))
    return ArtifactSource(**rsp.json())
