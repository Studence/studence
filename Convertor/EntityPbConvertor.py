class EntityPbConvertor:

    def convert(self, uipb, pb):
        uipb.id = pb.id;
        uipb.lifeTime = pb.lifeTime
        uipb.locale.defaultTimeZone = pb.locale.defaultTimeZone
