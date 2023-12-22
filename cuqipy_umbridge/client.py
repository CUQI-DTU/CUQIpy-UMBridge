""" CUQIpy-UMBridge client. Allows CUQIpy to communicate with the UM Bridge servers via HTTP. """

import umbridge
import cuqi


def get_supported_models(url:str):
    """ Get the list of supported models from the UM Bridge server. """

    return umbridge.supported_models(f"{url}:4242")


def create_Distribution(url:str, logpdf_model:str):
    """ Create a new CUQI distribution based on a server-side umbridge model. """

    model = umbridge.HTTPModel(f"{url}:4242", logpdf_model)

    # Get sizes
    input_sizes = model.get_input_sizes()
    output_sizes = model.get_output_sizes()

    if len(output_sizes) > 1:
        raise NotImplementedError("Models with multiple outputs are not supported.")
    if len(input_sizes) > 1:
        raise NotImplementedError("Models with multiple inputs are not supported.")

    return cuqi.distribution.UserDefinedDistribution(input_sizes[0], logpdf_func=model)

def create_Model(url:str, model:str):
    """ Create a new CUQI model based on a server-side umbridge model. """

    model = umbridge.HTTPModel(f"{url}:4242", model)

    # Get sizes
    input_sizes = model.get_input_sizes()
    output_sizes = model.get_output_sizes()

    if len(output_sizes) > 1:
        raise NotImplementedError("Models with multiple outputs are not supported.")
    if len(input_sizes) > 1:
        raise NotImplementedError("Models with multiple inputs are not supported.")

    return cuqi.model.Model(model, range_geometry=input_sizes[0], domain_geometry=output_sizes[0])







    
    
    