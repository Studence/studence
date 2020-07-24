from BaseCodeModule.BasePbIndexGenreator import BasePbIndexGenreator
from StudentModule.StudentConfig import StudentConfig


class StudentPbIndexGenreator(BasePbIndexGenreator):

    def genreateToPb(self, pb):
        map = self.genereate(pb=pb)
        map.put(StudentConfig.MILLISECONDS.value, pb.time.milliseconds)
        map.put(StudentConfig.ORGANISATION_ID.value, pb.classRef.schoolRef.organisation.id)
        map.put(StudentConfig.CLASS_ID.value, pb.classRef.id)
        map.put(StudentConfig.SCHOOL_ID.value, pb.classRef.schoolRef.id)
        map.put(StudentConfig.STUDENT_CODE.value, pb.studentCode)
        return map
