from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

add_io = ReqParser()
add_io.add_arguments(
    Argument(name="io_name", required=True, help="io name"),
    Argument(name="tool_name", required=True, help="io tool's name"),
    Argument(name="io_params", required=True, help="io parameters")
)

update_io = ReqParser()
update_io.add_arguments(
    Argument(name="io_name", required=True, help="io name"),
    Argument(name="tool_name", required=True, help="io tool's name"),
    Argument(name="io_params", required=True, help="io parameters")
)

delete_io = ReqParser()
delete_io.add_arguments(
    Argument(name="io_name", required=True, help="io name"),
)

get_io = ReqParser()
get_io.add_arguments(
    Argument(name="io_name", required=False, help="io name"),
    Argument(name="tool_name", required=False, help="io tool's name"),
    Argument(name="io_params", required=False, help="io parameters"),
    Argument(name="page", required=True, help="current page number"),
    Argument(name="per_page", required=True, default=30, help="every page size")
)
