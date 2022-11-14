from typing import Union, Dict, Literal

DisambiguationTripleDict = Dict[str, Union[str, 'DisambiguationTripleDict']]

DisambiguationValidationStatus = Literal["ACCEPTED", "REJECTED", "PENDING", "INVALID", "PAUSED"]
