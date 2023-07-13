from ..rest_adapter import RestAdapter as RestAdapter
from ..known_servers import XG_EXTERNOS as BASE_URL

rest_adapter = RestAdapter(BASE_URL)


from . import lines
from . import stops
from . import operators
from . import trips
from . import warning_alerts

__all__ = ["lines", "stops", "operators", "trips", "warning_alerts"]