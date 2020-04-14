from google.protobuf.json_format import MessageToJson

from CommonCode.strings import Strings


class AccountDetailsPbComparetor:

    def compare(self, newPb, oldPb):
        if (Strings.notEmpty(oldPb.accountNo)):
            if (Strings.notEmpty(newPb.accountNo)):
                oldPb.accountNo = newPb.accountNo
            else:
                raise Exception('Account Number Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.ifscCode)):
            if (Strings.notEmpty(newPb.ifscCode)):
                oldPb.ifscCode = newPb.ifscCode
            else:
                raise Exception('Ifsc Code Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.recipientName)):
            if (Strings.notEmpty(newPb.recipientName)):
                oldPb.recipientName = newPb.recipientName
            else:
                raise Exception('Racipent Name Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.bankName)):
            if (Strings.notEmpty(newPb.bankName)):
                oldPb.bankName = newPb.bankName
            else:
                raise Exception('Bank Name Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.branch)):
            if (Strings.notEmpty(newPb.branch)):
                oldPb.branch = newPb.branch
            else:
                raise Exception('Branch Cannot be empty' + MessageToJson(newPb))

        if (Strings.notEmpty(oldPb.googlePay.upiId)):
            if (Strings.notEmpty(newPb.googlePay.upiId)):
                oldPb.googlePay.upiId = newPb.googlePay.upiId
            else:
                raise Exception('Google pay Cannot be empty' + MessageToJson(newPb))
