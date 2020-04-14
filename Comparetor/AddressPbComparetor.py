from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings


class AddressPbComparetor:

    def compare(self, oldPb, newPb):
        if (Strings.notEmpty(oldPb.street)):
            if (Strings.notEmpty(newPb.street)):
                oldPb.street = newPb.street
            else:
                raise Exception('street Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.landmark)):
            if (Strings.notEmpty(newPb.landmark)):
                oldPb.landmark = newPb.landmark
            else:
                raise Exception('landmark Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.area)):
            if (Strings.notEmpty(newPb.area)):
                oldPb.area = newPb.area
            else:
                raise Exception('Area Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.city)):
            if (Strings.notEmpty(newPb.city)):
                oldPb.city = newPb.city
            else:
                raise Exception('city Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.state)):
            if (Strings.notEmpty(newPb.state)):
                oldPb.state = newPb.state
            else:
                raise Exception('state Cannot be empty' + MessageToJson(newPb))
