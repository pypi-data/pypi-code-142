try:
    import elasticsearch

    from .engine import EngineConfig, ElasticSearchBackend, ElasticSearchEngine
    from .settings import ElasticSearchSettings

    USE_ES = True

except ImportError:
    USE_ES = False
