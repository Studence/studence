from BaseCodeModule.BasePbIndexGenreator import BasePbIndexGenreator
from ClassModule.ClassConfig import ClassConfig


class ClassPbIndexGenerator(BasePbIndexGenreator):

    def genreateToPb(self, pb):
        map = self.genereate(pb=pb)
        map.put(ClassConfig.MILLISECONDS.value, pb.time.milliseconds)
        map.put(ClassConfig.CLASS_CODE.value, pb.classCode)
        map.put(ClassConfig.CLASS_TYPE.value, pb.classType)
        map.put(ClassConfig.SECTION_TYPE.value, pb.sectionType)
        map.put(ClassConfig.SCHOOL_ID.value, pb.schoolRef.id)
        map.put(ClassConfig.ORGANISATION_ID.value, pb.schoolRef.organisation.id)
        return map
