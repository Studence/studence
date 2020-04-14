class EntityUiPbUpdator:

    def update(self, pb, uipb):
        pb.id = uipb.id;
        pb.lifeTime = uipb.lifeTime
        pb.locale.defaultTimeZone = uipb.locale.defaultTimeZone
