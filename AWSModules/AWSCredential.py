class AWSCredential:
    m_accessKeyid = "Test"
    m_accessSecretKeyId = "Test"

    def getAccessKey(self):
        return self.m_accessKeyid

    def getAccessSecretKey(self):
        return self.m_accessSecretKeyId
