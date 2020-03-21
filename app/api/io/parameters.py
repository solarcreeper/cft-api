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
    Argument(name="page", required=True, default=1, help="current page number"),
    Argument(name="per_page", required=True, default=30, help="every page size")
)

add_his_io = ReqParser()
add_his_io.add_arguments(
    Argument(name="io_name", required=True, help="io name"),
    Argument(name="tool_name", required=True, help="io tool's name"),
    Argument(name="io_params", required=True, help="io parameters"),
    Argument(name="device_model", required=True, help="device model"),
    Argument(name="device_version", required=True, help="device version"),
    Argument(name="script_name", required=True, help="script name"),
    Argument(name="date", required=True, help="record date"),
    Argument(name="result", required=True, help="io result"),
)

get_his_io = ReqParser()
get_his_io.add_arguments(
    Argument(name="io_name", required=False, help="io name"),
    Argument(name="tool_name", required=False, help="io tool's name"),
    Argument(name="io_params", required=False, help="io parameters"),
    Argument(name="device_model", required=False, help="device model"),
    Argument(name="device_version", required=False, help="device version"),
    Argument(name="script_name", required=False, help="script name"),
    Argument(name="date", required=False, help="record date"),
    Argument(name="result", required=False, help="io result"),
    Argument(name="page", required=True, default=1, help="current page number"),
    Argument(name="per_page", required=True, default=30, help="every page size")
)

del_his_io = ReqParser()
del_his_io.add_arguments(
    Argument(name="io_name", required=True, help="io name")
)
