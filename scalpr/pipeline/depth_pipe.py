from typing import List, Tuple

from ..database.depth import Depth
from ..database.window import Window
from .pipe import Pipe


class DepthPipe(Pipe):


    def parse(self, payload: Tuple[List[List], List[List]]) -> Depth:
        pass

 
    def insert_in_first_timeframe(self, parsed: Depth, window: Window) -> Window:
        pass


    def insert_in_previous_timeframe(self, parsed: Depth, window: Window) -> Window:
        pass


    def insert_in_current_timeframe(self, parsed: Depth, window: Window) -> Window:
        pass

    
    def insert_in_next_timeframe(self, parsed: Depth, window: Window) -> Window:
        pass
