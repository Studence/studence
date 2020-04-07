from Environment.EnvironmentTypeEnum import EnvironmentTypeEnum


class ServerListner:
    m_currentServerEnvironment = None

    def __init__(self):
        self.m_currentServerEnvironment = EnvironmentTypeEnum.DEVEL

    def getServerEnvironment(self):
        return self.m_currentServerEnvironment
