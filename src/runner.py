from pathlib import Path

from src.algorithms.demds import DemDSRunner
from src.algorithms.numds import NuMDSRunner


ALGORITHMS = {
    "DemDS": DemDSRunner(),
    "NuMDS": NuMDSRunner(),
}


def run_instance(
    instance_dir,
    beta,
    seed,
    time_limit,
    algorithms=ALGORITHMS,
):
    results = []

    instance_name = Path(instance_dir).name

    for algorithm in algorithms.values():

        result = algorithm.run(
            instance_dir=instance_dir,
            seed=seed,
            time_limit=time_limit,
        )
        
        result["instance"] = instance_name
        result["beta"] = beta

        results.append(result)

    return results