from .CoreATASApi import CoreATASApi


def init(endpoints, token, launch_name, executor):
    return CoreATASApi.init_result(endpoints, token, launch_name, executor)


def upload_result(endpoints, token, execution_id, case_name, step_desc, step_status, case_status, executor, path,
                  screenshot,
                  attachment, start_time, end_time):
    data = {'caseName': case_name,
            'path': path,
            'stepStatus': step_status,
            'stepDescription': step_desc,
            'caseStatus': case_status,
            'executor': executor,
            'screen_path': screenshot,
            'attachment_path': attachment,
            'executionId': execution_id,
            'startTime': start_time,
            'endTime': end_time}
    CoreATASApi.save_result(endpoints, token, data)


def complete(endpoints, token, execution_id, case_status):
    CoreATASApi.run_complete(endpoints, token, execution_id, case_status)
