from abc import ABC, abstractmethod
from pathlib import Path


class AlgorithmRunner(ABC):

    def __init__(self, name, executable, filename):
        self.name = name
        self.executable = Path(executable)
        self.filename = filename

    def graph_file(self, instance_dir):
        return Path(instance_dir) / self.filename

    @abstractmethod
    def run(self, instance_dir, seed, time_limit):
        pass