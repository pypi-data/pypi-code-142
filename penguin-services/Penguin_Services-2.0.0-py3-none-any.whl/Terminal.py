from typing import List

class Terminal:
    # Magic terms == ['q', '-q', '--q', 'quit', '-quit', '--quit']
    def __init__(self, functionMappings: dict, prompt = "Threat$ecur3d$ ", errorMessage = "Did not understand that!"): 
        self.running = True
        self.functionMappings = functionMappings
        self.prompt = prompt
        self.errorMessage = errorMessage

    def start(self):
        while self.running:
            line = input(self.prompt)
            line = line.split()

            try:
                for arg in line:
                    if arg in ['q', '-q', '--q', 'quit', '-quit', '--quit']:
                        self.running = False
                        break

                idx = line[0]
                func = self.functionMappings[idx]
                return func(line[1:])
            except:
                print(self.errorMessage)
