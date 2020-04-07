class TimePbConvertor:

    def convert(self, uipb, pb):
        uipb.date = pb.date
        uipb.month = pb.month
        uipb.year = pb.year
        uipb.milliseconds = pb.milliseconds
        uipb.formattedDate = pb.formattedDate
        uipb.timezone = pb.timezone
        return
