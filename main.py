from application.application import MathGameApp
from dependencies import AppData

if __name__ == '__main__':
    AppData.application = MathGameApp()
    AppData.application.run()
