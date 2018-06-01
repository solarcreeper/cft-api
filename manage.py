from app import create_app


if __name__ == '__main__':
    app = create_app('development')
    app.debug = True
    app.run()