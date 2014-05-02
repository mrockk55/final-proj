import pickle

import net










if __name__ == "__main__":


  f = net.MLP(2,12,4)

  print f
  func = []
  for line in open( "train_data.csv" ):

    toks = line.split( "," )
    func.append( ( [float(toks[0]), float(toks[1])], int(toks[2] )))
    f.update( func[0][0], func[0][1] )

  accuracies = [-1 for i in range(  len( func )) ]

  for i in range( 10001 ):
  # for i in range( 10001 ):
    for (inps, out) in func:
      f.update( inps, out)

    correct, count = 0, 0
    for (inps, out) in func:
      oclass = f.outputClass( inps )
      # print (inps, out, oclass )
      if oclass == out:
        correct += 1
        # print "match"
      count += 1
    # raw_input()
    accuracies[correct] = i
    if i == 10 or i == 100 or i == 1000 or i == 10000:
      print "epoch: " , i
      print "%d / %d" % (correct, count )
      dmp = { "hiddens": f.hiddens, "outputs": f.outputs }
      pickle.dump( f , open('mlp' + str(i) + '.p', 'wb' ), 0 )


  print accuracies
