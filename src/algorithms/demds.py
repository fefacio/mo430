import subprocess
import time

from .base import AlgorithmRunner
from src.config import PROJECT_ROOT

class DemDSRunner(AlgorithmRunner):

    def __init__(
        self,
        executable="algorithms/DemDS/DemDS",
        filename="demds.txt",
        alpha=90,
    ):
        super().__init__(
            name="DemDS",
            executable=executable,
            filename=filename,
        )

        self.alpha = alpha

    def run(self, instance_dir, seed, time_limit):

        graph_file = self.graph_file(instance_dir)

        command = [
            str(self.executable),
            str(graph_file),
            str(seed),
            str(time_limit),
            str(self.alpha),
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

            # DemDS output:
            # <file>,<result>,<time>

            output = process.stdout.strip().splitlines()[-1]

            _, result, reported_time = output.split(",")

            return {
                "algorithm": self.name,
                "result": int(result),
                "time": elapsed,
                "reported_time": float(reported_time),
                "seed": seed,
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