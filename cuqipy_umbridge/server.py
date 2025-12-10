import umbridge
import cuqi
import numpy as np

def serve_distribution(distribution:cuqi.distribution.Distribution, port:int=4242):
    """ Serve a CUQI distribution via HTTP. """
    
    class DistributionModel(umbridge.Model):
        """ A model that wraps a CUQI distribution. """
        
        def __init__(self, name):
            super().__init__(name)
            self.distribution = distribution

        def get_input_sizes(self, config):
            return [self.distribution.dim]
        
        def get_output_sizes(self, config):
            return [1]
        
        def __call__(self, parameters, config):
            output = self.distribution.logpdf(np.asarray(parameters[0]))
            return [[output[0]]]
        
        def gradient(self, out_wrt, in_wrt, parameters, sens, config):
            output = self.distribution.gradient(np.asarray(parameters[0])) * sens
            return output.tolist()
        
        def supports_evaluate(self):
            return True
        
        def supports_gradient(self):
            # Attempt to evaluate the gradient
            try:
                self.distribution.gradient(np.ones(self.distribution.dim))
                return True
            except NotImplementedError:
                return False
            
    model_distribution = DistributionModel(distribution.__class__.__name__)

    umbridge.serve_models([model_distribution], port=port)


def serve_model(model:cuqi.model.Model, port:int=4242):
    """ Serve a CUQI model via HTTP. """
    
    class ModelModel(umbridge.Model):
        """ A model that wraps a CUQI model. """
        
        def __init__(self, name):
            super().__init__(name)
            self.model = model

        def get_input_sizes(self, config):
            return [self.model.domain_dim]
        
        def get_output_sizes(self, config):
            return [self.model.range_dim]
        
        def __call__(self, parameters, config):
            output = self.model.forward(np.asarray(parameters[0]))
            return [output.tolist()]
        
        def gradient(self, out_wrt, in_wrt, parameters, sens, config):
            output = self.model.gradient(np.asarray(parameters[0]), sens) # Todo: check this
            return output.tolist()
        
        def supports_evaluate(self):
            return True
        
        def supports_gradient(self):
            # Attempt to evaluate the gradient
            try:
                self.model.gradient(np.ones(self.model.domain_dim), np.ones(self.model.domain_dim))
                return True
            except NotImplementedError:
                return False
            
    model_model = ModelModel(model.__class__.__name__)

    umbridge.serve_models([model_model], port=port)
            
