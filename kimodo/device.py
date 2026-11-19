# SPDX-License-Identifier: Apache-2.0
"""Select a PyTorch device for local motion generation."""

import os
from typing import Optional

import torch


def select_device(requested: Optional[str] = None) -> str:
    """Select CUDA, Apple Metal, or CPU, with an explicit override."""
    name = requested or os.environ.get("KIMODO_DEVICE") or "auto"
    if name == "auto":
        if torch.cuda.is_available():
            return "cuda:0"
        return "mps" if torch.backends.mps.is_available() else "cpu"

    device = torch.device(name)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise ValueError("CUDA was requested but is unavailable")
    if device.type == "mps" and not torch.backends.mps.is_available():
        raise ValueError("Apple Metal was requested but is unavailable")
    if device.type not in {"cpu", "cuda", "mps"}:
        raise ValueError(f"Unsupported inference device: {name}")
    return str(device)
