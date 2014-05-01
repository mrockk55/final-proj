import math

import random

def crossProduct( left, right ):
  assert( len(left) == len(right) )
  agg = 0
  for i in range( len(left) ):
    agg += left[i] * right[i]

  return agg

assert( crossProduct( [3,2,1], [4,2,3] ) == 19 )
assert( crossProduct( [1], [1] ) == 1 )



def sigmoid( x ):
  return 1 / (1 + math.e ** (-1 * x) )


class MLP:

  __slots__ = ("ninputs", "hiddens", "outputs")


  def __init__( self, ninput, nhidden, noutput ):
    """construct and MLP with the given number of input, hidden and output nodes"""

    self.ninputs = ninput
    self.hiddens = [ [random.random() for i in range(ninput + 1)] for i in range( nhidden ) ]
    self.outputs = [ [random.random() for i in range( nhidden + 1) ] for i in range( noutput ) ]

  def values(self,  inputs ):
    """return a tuple containing the hidden values and the output values"""
    a_mid = [ sigmoid( crossProduct( [(1)] + inputs, W ) ) for W in self.hiddens ]


    a_fin = [ sigmoid( crossProduct( [(1)] + a_mid, W )  ) for W in self.outputs ]

    return (a_mid, a_fin)

  def __str__( self ):
    hidden = " : ".join(  [ ",".join( ["%.3f" % i for i in j ] ) for j in self.hiddens ] )
    output = " : ".join(  [ ",".join( ["%.3f" % i for i in j ] ) for j in self.outputs ] )

    return "Output Weights: " +  output + "\nHidden Weights: " + hidden


  def update( self, inputs, oclass ):
    ALPHA = .1

    idealResultVector = [1 if i == oclass - 1 else 0 for i in range( len( self.outputs ) ) ]
    # print "inputs ", inputs
    # print "idealResultVector ", idealResultVector

    (midvalues, outvalues) = self.values( inputs )

    # print "MLP ", str( self )

    # print "Hidden values ",  str( ["%.4f"  % i  for i in midvalues] )
    # print "Output values ",  str( ["%.4f"  % i  for i in outvalues] )


    # print "Middle Values ", midvalues  # str([".4f" % i for i in midvalues ])

                       # error                                # sigmoid derivative
    output_update = [ (outvalues[i] - idealResultVector[i]) * (outvalues[i]) * (1 - outvalues[i] ) for i in range(len(outvalues)) ]



    middle_update = [ ]
    # get the update for the bias layer
    # # middle_update.append(  sum( [output_update[i] * self.outputs[i][0] for i in range( len(self.outputs) ) ] ) )

    for j in range( len( self.hiddens ) ):
      u = 0
      for i in range( len(self.outputs ) ):
        u += output_update[i] * outvalues[i]

      u  *= midvalues[j] * (1 - midvalues[j])
      middle_update.append( u )






    # update the midde-to-output weights
    # do the bias input weights
    for o in range( len( self.outputs ) ):
       self.outputs[o][0] = self.outputs[o][0] - ALPHA * output_update[o] * 1
    # now do the weights with
    for o in range( len( self.outputs ) ):
      for m in range( 0, len( self.hiddens  )  ):
        self.outputs[o][m + 1] = self.outputs[o][m + 1] - ALPHA * output_update[o] * midvalues[m]

    # update the input-to-hidden layer
    # do the bias input weights
    for m in range( len(self.hiddens) ):
        self.hiddens[m][0] = self.hiddens[m][0] - ALPHA * middle_update[m] * 1

    for i in range( self.ninputs ):
      for h in range( len( self.hiddens ) ):
        self.hiddens[h][i + 1] = self.hiddens[h][i + 1] -  ALPHA * middle_update[h] * inputs[i]


  def outputClass( self, inputs ):
    _, outs = self.values( inputs )
    best = 0
    besti = 0

    for i in range( len( outs ) ):
      if outs[i] > best:
        best = outs[i]
        besti = i
    return besti

f = MLP(2,2,4)
func = []
for line in open( "test_data.csv" ):

  toks = line.split( "," )
  func.append( ( [float(toks[0]), float(toks[1])], int(toks[2] )))




if __name__ == "__main__":
  f.update( func[0][0], func[0][1] )

  for i in range( 10):
    for (inps, out) in func:
      f.update( inps, out)

    print "epoch: " , i
    correct, count = 0, 0
    for (inps, out) in func:
      oclass = f.outputClass( inps )
      # print (inps, out, oclass )
      if oclass == out:
        correct += 1
        # print "match"
      count += 1
    # i = raw_input()
    print "%d / %d" % (correct, count )

