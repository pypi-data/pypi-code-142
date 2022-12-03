from tcw import create_app
from tcw.config import Development, Production

if __name__ == '__main__':
    app = create_app(Development.PROJECT, Development)
    app.run()
