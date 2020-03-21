from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

add_script = ReqParser()
add_script.add_arguments(
    Argument(name="script_name", required=True, help="script name"),
    Argument(name="script_path", required=True, help="script_path"),
    Argument(name="script_params", required=False, help="script tool's name"),
    Argument(name="classification", required=True, help="script tool's name"),
    Argument(name="script_desc", required=True, help="script tool's name"),
)

delete_script = ReqParser()
delete_script.add_arguments(
    Argument(name="script_name", required=True, help="script name"),
)

get_script = ReqParser()
get_script.add_arguments(
    Argument(name="script_name", required=False, help="script name"),
    Argument(name="script_path", required=False, help="script_path"),
    Argument(name="script_params", required=False, help="script tool's name"),
    Argument(name="classification", required=False, help="script tool's name"),
    Argument(name="script_desc", required=False, help="script tool's name"),
    Argument(name="page", required=True, default=1, help="current page number"),
    Argument(name="per_page", required=True, default=30, help="every page size")
)

add_his_script = ReqParser()
add_his_script.add_arguments(
    Argument(name="script_name", required=True, help="script name"),
    Argument(name="script_path", required=True, help="script_path"),
    Argument(name="script_params", required=False, help="script tool's name"),
    Argument(name="classification", required=True, help="script tool's name"),
    Argument(name="script_desc", required=True, help="script tool's name"),
    Argument(name="device_model", required=True, help="device model"),
    Argument(name="device_version", required=True, help="device version"),
    Argument(name="date", required=True, help="record date"),
    Argument(name="result", required=True, help="script result"),
)

get_his_script = ReqParser()
get_his_script.add_arguments(
    Argument(name="script_name", required=False, help="script name"),
    Argument(name="script_path", required=False, help="script_path"),
    Argument(name="script_params", required=False, help="script tool's name"),
    Argument(name="classification", required=False, help="script tool's name"),
    Argument(name="script_desc", required=False, help="script tool's name"),
    Argument(name="device_model", required=False, help="device model"),
    Argument(name="device_version", required=False, help="device version"),
    Argument(name="date", required=False, help="record date"),
    Argument(name="result", required=False, help="script result"),
    Argument(name="page", required=True, default=1, help="current page number"),
    Argument(name="per_page", required=True, default=30, help="every page size")
)

del_his_script = ReqParser()
del_his_script.add_arguments(
    Argument(name="script_name", required=True, help="script name")
)
