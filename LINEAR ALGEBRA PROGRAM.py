# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 08:13:57 2022

@author: daiml
"""
from array import *
import numpy as np
import math

print('Vector Calculator')
print()
X = 0
while True:
    X = X + 1
    def vector_1():
    
        u = array('i', [])
    
        arr_length_u = int(input('Enter the length of u:\n'))
    
        for i in range(arr_length_u):
            x = int(input('Enter the next values:\n'))
            u.append(x)
        return u
    
        print(u)
    
    vector_u = vector_1()
    print()
    def vector_2():
       
        v = array('i', [])
    
        arr_length_v = int(input('Enter the length of v:\n'))
    
        for i in range(arr_length_v):
            x = int(input('Enter the next values:\n'))
            v.append(x)
        return v
        
        print(v)
    
    vector_v = vector_2()
    
    
    if len(vector_u) != len(vector_v):
        name = False
        print('Length of vectors have to match. Please try again.')
        continue    
    else:
        Y = 0
        while True:
            Y = Y + 1
            def norm_of_v():
                
                square_v = np.square(vector_v)
            
                sum_v = sum(square_v)
                return sum_v
                print(sum_v)
                       
            norm_v = norm_of_v()
            
            def dot_vector():
                dot_product = np.dot(vector_u, vector_v)
                return dot_product
                
                print(dot_product)
            
            dot_product = dot_vector()
            
            def projection_vector():
                proj_u = dot_product/norm_v
                return proj_u
                print(proj_u)
                
            projection_vect = projection_vector()
            print()
            def final_proj():
                arr_v = vector_v
                
                final_arr = [i * projection_vect for i in arr_v]
                
                print('The answer is: \n' + str(final_arr))
                
            final_proj()
            break
        
        break
    
    break
   

    
    



    

