class SpiInfoRepresentation:
    def __init__(self, internal, providers):
        self.internal = internal
        self.providers = providers

    def __str__(self):
        return f"SpiInfoRepresentation(" \
               f"internal={self.internal}" \
               f"providers={self.providers}" \
               f")"

    def get_post_data(self):
        import json
        return json.dumps({
            "internal": self.internal,
            "providers": self.providers,
        })

def construct_spi_info_representation(item):
    return SpiInfoRepresentation(
        internal=item.get("internal"),
        providers=item.get("providers"),
    )
