# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class ReportTask(object):

    def __init__(self, agent, taskType, progress, planId=None, startTime=None, endTime=None, success=None, errorMessage=None):
        """
        :param agent:  
        :param taskType:  
        :param planId: (Optional) 
        :param progress:  
        :param startTime: (Optional) 
        :param endTime: (Optional) 
        :param success: (Optional) 
        :param errorMessage: (Optional) 
        """

        self.agent = agent
        self.taskType = taskType
        self.planId = planId
        self.progress = progress
        self.startTime = startTime
        self.endTime = endTime
        self.success = success
        self.errorMessage = errorMessage
