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

"""Subtract a scalar from an event"""

from temporian.core import operator_lib
from temporian.core.data.event import Event
from temporian.core.operators.arithmetic_scalar.base import (
    BaseArithmeticScalarOperator,
)


class SubtractScalarOperator(BaseArithmeticScalarOperator):
    """
    Subtract a scalar from an event, feature to feature according to their
    position.
    """

    @classmethod
    @property
    def operator_def_key(cls) -> str:
        return "SUBTRACTION_SCALAR"

    @property
    def prefix(self) -> str:
        return "sub"


operator_lib.register_operator(SubtractScalarOperator)


def subtract_scalar(
    event: Event,
    value: any,
) -> Event:
    """
    Subtracts value from event.

    Args:
        event: Event to perform subtraction to.
        value: Scalar value to subtract from all event features.

    Returns:
        Event: Event with the subtraction of event features and value.
    """
    return SubtractScalarOperator(
        event=event,
        value=value,
    ).outputs["event"]
