from flask_restplus.reqparse import Argument

from app.api.reqparser import ReqParser

add_strategy = ReqParser()
add_strategy.add_arguments(
    Argument(name="strategy_name", required=True, help="strategy name"),
    Argument(name="owner", required=True, help="owner"),
    Argument(name="is_used", required=True, help="is used"),
    Argument(name="io_list", required=False, help="io_list"),
    Argument(name="script_list", required=False, help="script_list"),
    Argument(name="fault_list", required=False, help="fault_list"),
)

update_strategy = ReqParser()
update_strategy.add_arguments(
    Argument(name="strategy_name", required=True, help="strategy name"),
    Argument(name="owner", required=True, help="owner"),
    Argument(name="io_list", required=False, help="io_list"),
    Argument(name="script_list", required=False, help="script_list"),
    Argument(name="fault_list", required=False, help="fault_list"),
)

delete_strategy = ReqParser()
delete_strategy.add_arguments(
    Argument(name="strategy_name", required=True, help="strategy name"),
)

get_strategy = ReqParser()
get_strategy.add_arguments(
    Argument(name="strategy_name", required=False, help="strategy name"),
    Argument(name="owner", required=False, help="owner"),
    Argument(name="page", required=True, default=1, help="current page number"),
    Argument(name="per_page", required=True, default=30, help="every page size")
)
