import decimal
import json


class DecimalEncoder(json.JSONDecoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).decode(o)
