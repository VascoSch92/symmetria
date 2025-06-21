import time
import random
import statistics
from abc import abstractmethod
from typing import List
from dataclasses import field, dataclass

from symmetria import Permutation


@dataclass
class Result:
    entity_name: str
    execution_time: float
    standard_deviation: float
    min_time: float
    max_time: float


@dataclass
class Results:
    entity_name: List[str] = field(default_factory=list)
    execution_time: List[float] = field(default_factory=list)
    standard_dev: List[float] = field(default_factory=list)
    min_time: List[float] = field(default_factory=list)
    max_time: List[float] = field(default_factory=list)


class BenchmarkElement:
    @abstractmethod
    def run(self) -> Results:
        pass

    def _get_random_array(self) -> List[int]:
        length = random.randint(1, 1000000)
        elements = list(range(1, length + 1))
        random.shuffle(elements)

        return elements


@dataclass(frozen=True, slots=True, kw_only=True)
class PermutationBenchmark(BenchmarkElement):
    def run(self) -> Results:
        results = Results()

        elements: list[Permutation] = []
        execution_times: List[float] = []
        for _ in range(1_000):
            start_time = time.time()
            elements.append(Permutation(*self._get_random_array()))
            end_time = time.time()

            execution_times.append(end_time - start_time)
        result = Result(
            entity_name="Permutation",
            execution_time=statistics.mean(execution_times),
            standard_deviation=statistics.stdev(execution_times),
            min_time=min(execution_times),
            max_time=max(execution_times),
        )
        print(result)

        return results


@dataclass(frozen=True, slots=True)
class Benchmark:
    date: str

    def run(self) -> None:
        pass
