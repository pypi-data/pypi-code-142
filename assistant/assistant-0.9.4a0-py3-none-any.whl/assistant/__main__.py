import sys
import asyncio
from assistant.main import main

asyncio.run(main(sys.argv[1:]))