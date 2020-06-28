from BaseCodeModule.UpdateListnerCF import UpdateListnerCF


class UpdateListner:
    m_argsList = None

    def __init__(self, *argv):
        self.m_argsList = argv

    def listenUpdate(self, pb):
        updateListnerCf = UpdateListnerCF(self.m_argsList)
        updateListnerCf.start(pb=pb)
        return updateListnerCf.done()
