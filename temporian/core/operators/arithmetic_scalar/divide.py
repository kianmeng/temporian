# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Division Scalar Operator"""

from temporian.core import operator_lib
from temporian.core.data import dtype
from temporian.core.data.event import Event
from temporian.core.operators.arithmetic_scalar.base import (
    BaseArithmeticScalarOperator,
)


class DivideScalarOperator(BaseArithmeticScalarOperator):
    """
    Divides event by a scalar value.
    """

    def __init__(
        self,
        event: Event,
        value: any,
    ):
        super().__init__(event, value)

        # Assuming previous dtype check of event_1 and event_2 features
        for feat in event.features:
            if feat.dtype in [dtype.INT32, dtype.INT64]:
                raise ValueError(
                    "Cannot use the divide operator on feature "
                    f"{feat.name} of type {feat.dtype}. Cast to "
                    "a floating point type or use "
                    "floordiv operator (//) instead on integer features."
                )

    @classmethod
    @property
    def operator_def_key(cls) -> str:
        return "DIVISION_SCALAR"

    @property
    def prefix(self) -> str:
        return "div"


operator_lib.register_operator(DivideScalarOperator)


def divide_scalar(
    numerator: Event,
    denominator: any,
) -> Event:
    """
    Divides and event and a scalar value.

    Args:
        numerator: Numerator event
        denominator: Denominator value
    Returns:
        Event: Division of numerator features and denominator value
    """
    return DivideScalarOperator(
        event=numerator,
        value=denominator,
    ).outputs["event"]
