import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:  
    our_array = np.array(list)
    our_array = our_array.reshape((3,3))

    mean1 = np.mean(our_array, axis=0)
    mean2 = np.mean(our_array, axis=1)
    mean3 = np.mean(our_array)
    mean = [mean1.tolist(), mean2.tolist(), mean3.tolist()]

    var1 = np.var(our_array, axis=0)
    var2 = np.var(our_array, axis=1)
    var3 = np.var(our_array)
    var = [var1.tolist(), var2.tolist(), var3.tolist()]

    std1 = np.std(our_array, axis=0)
    std2 = np.std(our_array, axis=1)
    std3 = np.std(our_array)
    std = [std1.tolist(), std2.tolist(), std3.tolist()]

    max1 = np.amax(our_array, axis=0)
    max2 = np.amax(our_array, axis=1)
    max3 = np.amax(our_array)
    max = [max1.tolist(), max2.tolist(), max3.tolist()]

    min1 = np.amin(our_array, axis=0)
    min2 = np.amin(our_array, axis=1)
    min3 = np.amin(our_array)
    min = [min1.tolist(), min2.tolist(), min3.tolist()]

    sum1 = np.sum(our_array, axis=0)
    sum2 = np.sum(our_array, axis=1)
    sum3 = np.sum(our_array)
    sum = [sum1.tolist(), sum2.tolist(), sum3.tolist()]

    calculations = {
      'mean' : mean,
      'variance' : var,
      'standard deviation' : std,
      'max' : max,
      'min' : min,
      'sum' : sum
    }

    return calculations