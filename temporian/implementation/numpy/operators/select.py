from typing import Dict

from temporian.core.operators.select import SelectOperator
from temporian.implementation.numpy import implementation_lib
from temporian.implementation.numpy.data.event import IndexData
from temporian.implementation.numpy.data.event import NumpyEvent
from temporian.implementation.numpy.operators.base import OperatorImplementation


class SelectNumpyImplementation(OperatorImplementation):
    """Select a subset of features from an event."""

    def __init__(self, operator: SelectOperator) -> None:
        super().__init__(operator)
        assert isinstance(operator, SelectOperator)

    def __call__(self, event: NumpyEvent) -> Dict[str, NumpyEvent]:
        # gather operator attributes
        feature_names = self._operator.feature_names

        # get feature indexes to be selected
        feature_idxs = [
            event.feature_names.index(feature_name)
            for feature_name in feature_names
        ]
        # create output event
        output_event = NumpyEvent(
            data={},
            feature_names=feature_names,
            index_names=event.index_names,
            is_unix_timestamp=event.is_unix_timestamp,
        )
        # select feature index key-wise
        for index_key, index_data in event.iterindex():
            output_event[index_key] = IndexData(
                [index_data.features[idx] for idx in feature_idxs],
                index_data.timestamps,
            )

        return {"event": output_event}


implementation_lib.register_operator_implementation(
    SelectOperator, SelectNumpyImplementation
)
