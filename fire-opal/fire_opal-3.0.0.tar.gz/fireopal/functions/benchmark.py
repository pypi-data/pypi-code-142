# Copyright 2022 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

from typing import Optional

from .base import fire_opal_workflow


@fire_opal_workflow("benchmark_workflow")
def benchmark(
    ibm_device_name: str,
    config_file: str,
    hub: str,
    group: str,
    project: str,
    ibmq_token: str,
    output_path: Optional[str] = None,
):
    """Runs the Fire Opal benchmark suite."""
    return {
        "ibm_device_name": ibm_device_name,
        "config_file": config_file,
        "hub": hub,
        "group": group,
        "project": project,
        "ibmq_token": ibmq_token,
        "output_path": output_path,
    }
