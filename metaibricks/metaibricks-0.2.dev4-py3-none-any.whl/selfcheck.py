"""Management of the self-tests of the library and of each module
"""

import sys

try:
    import metaibricks
except Exception as excpt:
    print("Failed to import metaibricks")
    print()
    print("Following Exception caught :")
    print()
    print(excpt)
    sys.exit(1)

if __name__ == "__main__":
    try:
        import metaibricks.extraction
        import metaibricks.pipeline
        import metaibricks.settings

        print(f"{metaibricks.__name__} ({metaibricks.__version__}): selfcheck OK.")
        sys.exit(0)

    except Exception as excpt:
        print(f"{metaibricks.__name__} ({metaibricks.__version__}): selfcheck failed.")
        print()
        print("Following Exception caught :")
        print()
        print(excpt)
        sys.exit(1)
