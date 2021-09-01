class NNL:
    def __init__(self, parentLayer=None, childLayer=None, linearOutput=False, useMomentum=False, momentumFactor=0.9) -> None:
        self.parentLayer        = parentLayer       #NNL
        self.childLayer         = childLayer        #NNL
        self.linearOutput       = linearOutput      #bool
        self.useMomentum        = useMomentum       #bool
        self.momentumFactor     = momentumFactor    #double
        self.numNodes           = None #int
        self.numChildNodes      = None #int
        self.numParentNodes     = None #int
        self.weights            = None #double**
        self.weightChanges      = None #double**
        self.neuronValues       = None #double*
        self.desiredValues      = None #double*
        self.errors             = None #double*
        self.biasWeights        = None #double*
        self.biasValues         = None #double*
        self.learningRate       = None #double*
    
    def initialize(self, parentNNLayer, childNNLayer):
        self.neuronValues = [0] * self.numNodes
        self.desiredValues = [0] * self.numNodes
        self.errors = [0] * self.numNodes
        

        self.parentLayer = parentNNLayer if parentNNLayer is not None else None

        if(childNNLayer is not None):
            self.childLayer = childNNLayer

            self.weights = [0] * self.numNodes
            self.weightChanges = [0] * self.numNodes

            for x in range(self.numNodes):
                self.weights[x] = [0] * self.numChildNodes
                self.weightChanges[x] = [0] * self.numChildNodes
            
            self.biasValues = [-1] * self.numChildNodes
            self.biasWeights = [0] * self.numChildNodes
    def cleanup():
        pass
    def randomizeWeights():
        pass
    def calculateErrors():
        pass
    def adjustWeights():
        pass
    def calculateNeuronValues():
        pass

class NN:
    def __init__(self, ipl: NNL, hdl: NNL, opl: NNL) -> None:
        self.inputLayer = ipl
        self.hiddenLayer = hdl
        self.outputLayer = opl
        pass
    def initialize(self,nNodesInput, nNodesHidden, nNodesOutput):
        self.inputLayer.numNodes = nNodesInput
        self.inputLayer.numChildNodes = nNodesHidden
        self.inputLayer.numParentNodes = 0
        self.inputLayer.initialize(None, self.hiddenLayer)
        self.inputLayer.randomizeWeights()

        self.hiddenLayer.numNodes = nNodesHidden
        self.hiddenLayer.numChildNodes = nNodesOutput
        self.hiddenLayer.numParentNodes = nNodesInput
        self.hiddenLayer.initialize(self.inputLayer, self.outputLayer)
        self.hiddenLayer.randomizeWeights()

        self.outputLayer.numNodes = nNodesOutput
        self.outputLayer.numChildNodes = 0
        self.outputLayer.numParentNodes = nNodesHidden
        self.outputLayer.initialize(self.hiddenLayer, None)

def main():

    #test = NN
    test = NNL(linearOutput=True, useMomentum=True, momentumFactor=0.91)
    test.numNodes = 2
    test.numChildNodes = 3
    test.initialize(None, None)
    print(test.weights)
    print(test.weightChanges)
    print(test.biasValues)
    print(test.biasWeights)
    # test.numNodes = 10
    # test.numChildNodes = 12
    # test.numParentNodes = 0
    # test.initialize(None, )
    # print(test.linearOutput)
    # print(test.parentLayer.useMomentum)
    # print(test.childLayer.useMomentum)

main()