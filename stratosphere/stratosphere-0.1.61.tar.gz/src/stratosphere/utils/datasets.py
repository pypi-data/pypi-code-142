from stratosphere.run import Run


def load_datasets(datasets):
    def func(run: Run):
        for key, key_type in key_types:
            assert_keys(name, key)
            if not isinstance(getattr(run, name)[key], key_type):
                raise RunAssertion(f"type(run.{name}) != {key_type}")

    return func
