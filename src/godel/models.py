from typing import Union, Dict, Literal

DisambiguationTripleDict = Dict[str, Union[str, 'DisambiguationTripleDict']]
PredicateWeightDict = Dict[str, float]

DisambiguationValidationStatus = Literal["ACCEPTED", "REJECTED", "PENDING", "INVALID", "PAUSED"]
