from tcw import create_app
from tcw.config import Development, Production

app = create_app(Production.PROJECT, Production)
# app = create_app(Development.PROJECT, Development)

if __name__ == '__main__':
    app.run()
