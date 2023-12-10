import pytorch

# A transformer neural network.

class Encoder(pytorch.nn.Module):
  def __init__(self, n, d, h):
    super().__init__()
    self.n = n
    self.d = d
    self.h = h
    self.w = pytorch.nn.Linear(d, h)
    self.u = pytorch.nn.Linear(h, h)
    self.v = pytorch.nn.Linear(h, d)
    self.e = pytorch.nn.Embedding(n, d)
    self.r = pytorch.nn.Linear(d, h)
    self.s = pytorch.nn.Linear(h, h)
    self.t = pytorch.nn.Linear(h, d)
    self.o = pytorch.nn.Linear(d, h)
    self.p = pytorch.nn.Linear(h, h)
    self.q = pytorch.nn.Linear(h, d)
    self.r = pytorch.nn.Linear(d, h)

class PositionalEncoding(pytorch.nn.Module):
  def __init__(self, d, p):
    super().__init__()
    self.d = d
    self.p = p
    self.e = pytorch.nn.Embedding(p, d)
    self.r = pytorch.nn.Linear(d, d)

class Transformer(pytorch.nn.Module):
  def __init__(self, n_in, n_out, n_heads, n_layers, n_units, dropout):
    super().__init__()
    self.n_in = n_in
    self.n_out = n_out
    self.n_heads = n_heads
    self.n_layers = n_layers
    self.n_units = n_units
    self.dropout = dropout

    self.norm = pytorch.nn.LayerNorm(n_in)
    self.pe = PositionalEncoding(n_in)
    self.encoder = Encoder(n_in, n_heads, n_layers,
    