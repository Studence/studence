import time


class TimeUtility:
    def getTimeUiPb(self, timeUiPb, timeZone):
        millis = self.getCurrentMillis()
        timeUiPb.milliseconds = millis
        timeUiPb.timezone = timeZone
        return self.getTimeUiPbWithCurrentTime(timeUiPb=timeUiPb,
                                               formattedDate=self.getCurrentTimethroughMillis(millis=millis))

    def getCurrentMillis(self):
        return int(time.time() * 1000.0)

    def getCurrentTimethroughMillis(self, millis):
        return time.strftime('%Y-%m-%d : %H:%M:%S', time.localtime(millis / 1000.0))

    def getTimeUiPbWithCurrentTime(self, timeUiPb, formattedDate):
        list = formattedDate.split()
        list2 = list[0].split('-')
        timeUiPb.year = list2[0]
        timeUiPb.month = list2[1]
        timeUiPb.date = list2[2]
        timeUiPb.formattedDate = formattedDate
        return timeUiPb
