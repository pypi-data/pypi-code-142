class ClientPolicyExecutorRepresentation:
    def __init__(self, configuration, executor):
        self.configuration = configuration
        self.executor = executor

    def __str__(self):
        return f"ClientPolicyExecutorRepresentation(" \
               f"configuration={self.configuration}" \
               f"executor={self.executor}" \
               f")"

    def get_post_data(self):
        import json
        return json.dumps({
            "configuration": self.configuration,
            "executor": self.executor,
        })

def construct_client_policy_executor_representation(item):
    return ClientPolicyExecutorRepresentation(
        configuration=item.get("configuration"),
        executor=item.get("executor"),
    )
