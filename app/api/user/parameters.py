from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

add_user = ReqParser()
add_user.add_arguments(
    Argument(name="username", required=True, help="username"),
    Argument(name="password", required=True, help="password")
)

update_user = ReqParser()
update_user.add_arguments(
    Argument(name="username", required=True, help="username"),
    Argument(name="password", required=True, help="password")
)

delete_user = ReqParser()
delete_user.add_arguments(
    Argument(name="username", required=True, help="username"),
)

get_user = ReqParser()
get_user.add_arguments(
    Argument(name="username", required=False, help="username"),
)