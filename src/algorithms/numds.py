import subprocess
import time

from .base import AlgorithmRunner
from src.config import PROJECT_ROOT

class NuMDSRunner(AlgorithmRunner):

    def __init__(
        self,
        executable="algorithms/NuMDS/NuMDS",
        filename="numds.txt",
    ):
        super().__init__(
            name="NuMDS",
            executable=executable,
            filename=filename,
        )

    def run(self, instance_dir, seed, time_limit):

        graph_file = self.graph_file(instance_dir)

        command = [
            str(self.executable),
            str(graph_file),
            str(time_limit),
            str(seed),
        ]

        start = time.perf_counter()

        try:
            process = subprocess.run(
                command,
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True,
                check=True,
            )

            elapsed = time.perf_counter() - start

            # NuMDS ouput:
            # <file> <seed> <result>

            output = process.stdout.strip().splitlines()[-1]

            _, output_seed, result = output.split()

            return {
                "algorithm": self.name,
                "result": int(result),
                "time": elapsed,
                "reported_time": None,
                "seed": int(output_seed),
                "status": "ok",
            }

        except subprocess.CalledProcessError as e:
            elapsed = time.perf_counter() - start

            return {
                "algorithm": self.name,
                "result": None,
                "time": elapsed,
                "reported_time": None,
                "seed": seed,
                "status": "error",
                "error": e.stderr or e.stdout or str(e),
            }

        except Exception as e:
            elapsed = time.perf_counter() - start

            return {
                "algorithm": self.name,
                "result": None,
                "time": elapsed,
                "reported_time": None,
                "seed": seed,
                "status": "error",
                "error": repr(e),
            }