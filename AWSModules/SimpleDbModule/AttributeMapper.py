from addict import Dict


class AttributeMapper:
    m_replace = False

    def mapper(self, name, value, bool=False):
        if (bool != None):
            self.m_replace = bool
        mapper = Dict()
        mapper.Name = name
        mapper.Value = value
        mapper.Replace = self.m_replace
        return mapper
