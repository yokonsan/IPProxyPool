from Api.api import app
from Schedule.schedule import Schedule


def main():
    s = Schedule()
    s.run()
    app.run()


if __name__ == '__main__':
    main()
