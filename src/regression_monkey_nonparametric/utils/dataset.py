# %%
import pathlib
from typing import Dict, List
from datetime import date
import yaml
from pydantic import BaseModel

from regression_monkey_nonparametric.utils.setup import git_path_setting

# --- Expose only DATASET_CONFIG ---
__all__ = ["DATASET_CONFIG"]

# Define multiple config paths
git_root = git_path_setting()
if git_root is None:
    raise RuntimeError("Not a git repository")
_config_path = pathlib.Path(git_root) / "dataset" / "config"
_CONFIG_FILES = str(_config_path / "dataset.yml")


class _DatasetField(BaseModel):
    description: str              # dataset description
    source_type: str                    # source_type, e.g. "BigQuery"
    source: str                   # source location
    comment: str                  # dataset comment
    metadata: Dict[str, List]  # column name and type
    updated_date: date            # tracking when last updated


class _DatasetConfig(BaseModel):
    dataset: Dict[str, _DatasetField]



# Load dataset configuration from YAML file
def _load_dataset_config(file_path: str) -> _DatasetConfig:
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return _DatasetConfig(**data)


# Create Config and CommandConfig instances
DATASET_CONFIG = _load_dataset_config(_CONFIG_FILES)
