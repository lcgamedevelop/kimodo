# Installation

> Note: This project will download and install additional third-party open source software projects. Review the license terms of these open source projects before use.

> Note: This repo was developed and primarily tested on Linux

There are two ways to install Kimodo: (1) as a package, or (2) download the source code and install.
Text-driven generation requires a Hugging Face token for the text encoder. Pose-only generation uses the motion checkpoint without loading the text encoder.

## Set Up Hugging Face Token

The Kimodo text encoder relies on the **gated** `meta-llama/Meta-Llama-3-8B-Instruct` model, which requires:
- Your HF account has been granted access to the [model page](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct).
- You provide a HF token for runtime

After receiving access to the Llama repo, please create an access token [here](https://huggingface.co/settings/tokens/new?tokenType=read). Then use it to log in on your command line:

```bash
hf auth login
```
or alternatively, paste the token in this file ``~/.cache/huggingface/token``. If you don't have `hf` installed, you will first need to run `pip install --upgrade huggingface_hub`.

## Kimodo Install Option 1: Package Install

The easiest way to get started is simply installing Kimodo as a package without needing to clone the codebase. This will allow you to generate motions and run the demo as a black box.

We suggest creating a new Python environment for the install, for example with `venv` or conda:
```bash
conda create -n kimodo python=3.10
conda activate kimodo
```

To ensure you have a version of [PyTorch](https://pytorch.org/get-started/locally/) that is compatible with your system and CUDA version, it is recommended to manually install the best version of PyTorch for you before installing Kimodo. Anything over PyTorch 2.0 is sufficient. We strongly suggest using a GPU-capable version of PyTorch to generate motions in a reasonable amount of time.

Installing the base Kimodo package will allow you generate motions with the command line:
```bash
pip install git+https://github.com/nv-tlabs/kimodo.git
```

If you want to be able to run the interactive demo as well, use this command which installs additional dependencies:
```bash
pip install "kimodo[all] @ git+https://github.com/nv-tlabs/kimodo.git"
```

Now should be ready to use Kimodo. Check out the [quick start guide](quick_start.md) to see how to generate motions.

If you experience issues with package or system compatibility using the above install strategy, we recommend downloading the codebase and using the Docker install detailed below.

## Kimodo Install Option 2: Source Code Install

If you plan to build on Kimodo or dig into the codebase, you'll want to clone and install the repo.

### Clone Kimodo Repository

```bash
git clone https://github.com/nv-tlabs/kimodo.git
cd kimodo
```

### Choose Your Installation Route
Kimodo can be installed by building and running through a virtual environment (e.g., `conda`) or within a Docker container.

### Apple Silicon

Install the Xcode command-line tools, CMake, and an arm64 Python with a Metal-enabled PyTorch build. With the environment active, run `pip install -e .` from the checkout. The motion correction build uses [SIMDe v0.8.2](https://github.com/simd-everywhere/simde/tree/71fd833d9666141edcd1d3c109a80e228303d8d7) on arm64.

The generation CLI selects Apple Metal when MPS is available. Pass `--device cpu` to use the CPU, or set `KIMODO_DEVICE` for a default for the CLI and interactive demo. Device arguments to the CLI take precedence.

Saved pose constraints can drive local generation directly:

```sh
kimodo_gen --pose-only --constraints constraints.json --device mps \
    --model Kimodo-SOMA-RP-v1.2 --duration 0.6 --bvh --output transition
```

Pose-only generation loads the motion checkpoint and uses the model's empty text condition. Text-driven generation uses the text encoder described above.

```{toctree}
:maxdepth: 1

installation_virtual_env
installation_docker
installation_smpl
```
