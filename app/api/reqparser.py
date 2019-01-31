from flask_restplus.reqparse import RequestParser


class ReqParser(RequestParser):
    def add_arguments(self, *args, **kwargs):
        for arg in args:
            self.add_argument(arg)

    def parse_args(self, req=None, strict=False, delete_none=False):
        result = super(ReqParser, self).parse_args(req, strict)
        if delete_none:
            for key in result.keys():
                if not result[key]:
                    result.pop(key, None)
        return result