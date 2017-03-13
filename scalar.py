import nengo

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=1, radius=10)
    
    stim = nengo.Node(1)
    
    nengo.Connection(stim, a)