
import Configurator


def main():
    """
    """
    config = Configurator.Configurator("./pycal.conf")
    pycal = config.configure()
    pycal.run()

if __name__ == "__main__":
    main()
