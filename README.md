# CUQIpy-UMBridge

Adds a bridge between CUQIpy and UM-Bridge allowing CUQIpy Models and Distributions to be served via an Um-Bridge server.

Also allows for the creation of a CUQIpy Model or Distribution from a UM-Bridge server url.

## Installation

To come.


## Usage

### Creating a CUQIpy Distribution from a UM-Bridge server url

```python
from cuqipy_umbridge.client import get_supported_models, create_distribution

# Server url
url = "http://localhost"

# Get a list of supported models
supported_models = get_supported_models(url)

# Create a CUQIpy Distribution from a UM-Bridge server url
distribution = create_distribution(url, supported_models[0])

```

### Creating a CUQIpy Model from a UM-Bridge server url

```python
from cuqipy_umbridge.client import get_supported_models, create_model

# Server url
url = "http://localhost"

# Get a list of supported models
supported_models = get_supported_models(url)

# Create a CUQIpy Model from a UM-Bridge server url
model = create_model(url, supported_models[1])

```

### Serving a Distribution via UM-Bridge
(Must run via command line)

```python
from cuqi.distribution import Gaussian
from cuqipy_umbridge.server import serve_distribution

# Gaussian distribution
dist = Gaussian(0, 1)

# Serve the distribution via UM-Bridge
serve_distribution(dist)

```

### Serving a Model via UM-Bridge
(Must run via command line)

```python
from cuqi.model import Deconvolution1D
from cuqipy_umbridge.server import serve_model

# Deconvolution forward model
model = Deconvolution1D().model

# Serve the model via UM-Bridge
serve_model(model)

```

