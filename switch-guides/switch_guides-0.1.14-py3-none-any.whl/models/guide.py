# -------------------------------------------------------------------------
# Copyright (c) Switch Automation Pty Ltd. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


from typing import List, Optional, Union
from pydantic import BaseModel
from .literals import STATUS_STATE
from .step import SwitchGuideStep, SwitchGuideStepComponent, SwitchGuideStepDefinitionUiAssets, SwitchGuideStepDependency, SwitchGuideStepOverrides


class SwitchGuideStatus(BaseModel):
    state: STATUS_STATE
    percentageCompleted: int = 0


class SwitchGuideDefinitionOptions(BaseModel):
    enable_live_notification: bool = False
    """Enable live notification for this Guide"""

    enable_debug_mode: bool = False
    """Enable debug mode for switch user.
    Provides additional elements on the UI to help with debugging.
    Such as logs associated with each individual step.
    """


class SwitchGuideSummaryStepEvents(BaseModel):
    """Events that can be triggered on the Summary Step
    """

    componentOnCompletion: Union[SwitchGuideStepComponent, None]
    """Defined component will be displayed on the Summary Step when the Guide is completed to 100%"""


class SwitchGuideSummaryStepConfigDefinition(BaseModel):
    """Configuration for the Summary Step"""

    uiAssets: Optional[SwitchGuideStepDefinitionUiAssets]
    """UI Assets associated with the Guide"""

    events: Optional[SwitchGuideSummaryStepEvents]
    """Events that can be triggered on the Summary Step"""


class SwitchGuideSummaryStepConfig(BaseModel):
    component: Optional[SwitchGuideStepComponent]
    uiAssets: Optional[SwitchGuideStepDefinitionUiAssets]

class SwitchGuideDefinition(BaseModel):
    """Definition of the Guide"""
    
    id: str = ''
    """Unique identifier for the Guide"""

    name: str
    """Name of the Guide"""

    description: str
    """Description of the Guide"""

    instructions: str
    """Instructions on how to use the Guide"""

    summaryStep: Optional[SwitchGuideSummaryStepConfigDefinition]
    """Configuration for the Summary Step"""
    
    steps: List[SwitchGuideStepDependency]
    """Steps associated with the Guide"""
    
    options: Optional[SwitchGuideDefinitionOptions]
    """Options for the Guide"""


class SwitchGuideInstance(BaseModel):
    id: str
    status: SwitchGuideStatus
    steps: List[SwitchGuideStepOverrides]


class SwitchGuide(SwitchGuideDefinition, SwitchGuideInstance, BaseModel):
    id: str
    summaryStep: Optional[SwitchGuideSummaryStepConfig]
    steps: List[SwitchGuideStep]


class SwitchGuideSummary(BaseModel):
    id: str
    journeyDefinitionId: str
    name: str
    createdOnUtc: str
    modifiedOnUtc: str
    description: str
    instructions: str
    status: SwitchGuideStatus
