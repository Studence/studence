from addict import Dict


class ExpectedMapper:
    m_replace = False

    def mapper(self, name, value, bool):
        if (bool != None):
            self.m_replace = bool
        mapper = Dict()
        mapper.Name = name
        mapper.Value = value
        mapper.Exists = self.m_replace
        return mapper
