import unittest
from net import *



class FeedForwardTest(unittest.TestCase):


  def test_cross_product( self ):
    self.assertEquals( crossProduct( [3,2,1], [4,2,3] ) , 19  )
    self.assertEquals( crossProduct( [1], [1] ) , 1  )

  def test_simple(self):
    net = MLP(2, 2, 1)
    net.hiddens = [ [1,1,1], [1,1,1] ]
    net.outputs = [ [1,1,1], [1,1,1] ]

    (mids, outs) = net.values( [1,1] )

    self.assertTrue( len(mids) == 2, "Mids wrong length" )
    self.assertTrue( len(outs) == 2, "Mids wrong length" )


    self.assertTrue( mids[0] == sigmoid( 3 ) )
    self.assertTrue( mids[1] == sigmoid( 3 ) )

    # expected out
    eout = 1 * sigmoid( 3 ) + 1 * sigmoid( 3 ) + 1 * 1
    self.assertTrue( outs[0] == sigmoid( eout ) )
    self.assertTrue( outs[1] == sigmoid( eout ) )




  def test_complex( self ):
    m = MLP( 2, 2, 1 )

    # 1 - 2 \
    #   X     5
    # 2 - 4 /


    m.hiddens = [ [.5, .7, .3], [.2, .3, 1] ]
    m.outputs = [ [.5, .1, 2 ] ]
    mids, outs = m.values( [2, -1] )

    exp2 = sigmoid(  (1 * .5) + (2 * .7) - (1 * .3) )
    self.assertTrue( exp2 == mids[0] )

    exp4 = sigmoid( (1 * .2) + (.3 * 2) - (1 * 1) )
    self.assertTrue( exp4 == mids[1] )

    exp5 = sigmoid( (1 * .5) + (.1 * mids[0]) + (2 * mids[1]) )

    self.assertTrue( exp5 == outs[0] )





  def test_backprop_full( self ):
    m = MLP(1,1,1)

    m.hiddens = [[.6, .5] ]
    m.outputs = [[.3, .2]]

    mids, outs = m.values ( [2] )


    m.update( [2], 2 )


    self.assertEquals( round( mids[0], 3 ), .832, "Middle layer is incorrect" )
    self.assertEquals( round( outs[0], 3 ), .615 , "Middle layer is incorrect" )

    self.assertEquals( round( m.outputs[0][0], 3 ), .285, "W53 is incorrect" )
    self.assertEquals( round( m.outputs[0][1], 3 ), .188, "W23 is incorrect" )

    self.assertEquals( round( m.hiddens[0][0], 2 ), .60, "W42 is incorrect" )
    self.assertEquals( round( m.hiddens[0][1], 2 ), .50, "W12 is incorrect" )


if __name__ == '__main__':
    unittest.main()

# make sure the shuffled sequence does
