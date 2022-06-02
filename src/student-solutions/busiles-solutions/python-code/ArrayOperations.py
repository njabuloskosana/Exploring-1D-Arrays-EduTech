from array import array
from ast import For
from distutils.command.build_scripts import first_line_re
import heapq
from operator import contains


class ArrayOperations:
    #The method sum will calculate the sum of all values 
    # in the array and return the sum, if the array is empty return zero
    # arr=[1,2,3,4] returns 10
        
    def sum(self,arr):
        # add code
        sum=0
        for i in arr:
            sum = sum + i
        return sum
        

    # The method average will calculate the average of all the values 
    # within the array an return the average if the array is empty
    # return zero
    # arr=[1,2,3,4] returns 2,5

    def average(self,arr):
        if arr==None:
            return 0 

        else:
            average = sum(arr) /len(arr)

        return average

    # The method contains returns true if value is found in the 
    # array and false if the value is not in the array
    # if the array is empty it returns zero
    # arr=[6,9,0,4] value=0 retur true

    def contains(self,arr,value):
        if arr==None:
            return 0

        else:
            for x in arr:
                
                if x == value:
                  return True


    # This method removes value from the array and returns back 
    # a new array without the value, if the value is not present
    # the original array is returned, if the array is empty return 
    # null
    # arr=[6,7,8,4,9,0] and value=8 return [6,7,4,9,0] 
    
    def remove(self,arr,value):
        if arr==None:
            return 0
        else:
            if contains(arr,value)==True:
                arr.remove(value)
                return arr
            else:
                return arr

    # This method finds the highest value in the array and returns
    # the value, if the array is empty return zero
    # arr=[9,7,4,3] return 9
        
    def maximum(self,arr):
        if arr==None:
            return 0
        else:
            maximum=max(arr)
            return maximum





    #This method finds the lowest value in the array and returns
    # the value, if the array is empty return zero 
    # arr=[5,4,1,9] return 1

    def minimum(self,arr):
        if arr==None:
            return 0
        else:
            minimum=min(arr)
            return minimum

    # This method find the second lowest value in the array
    # and returns the value, if the array is empty return 
    # zero arr=[1,4,3,2] returns 2

    def secondSmallest(self,arr):
        if arr==None:
            return 0

    def second_smallest(numbers):
            return heapq.nsmallest(2, numbers)[-1]



    # This method returns the reversed version of the array
    # [1,2,3,4] becomes [4,3,2,1], if the array is empty
    # return null
        
    def reverse(self,arr):
        if arr==None:
           return 0
        else:
            arr.reverse() 
            return arr 
    

    # This method recieves an array with duplicate values and 
    # returns a new array without duplicates [1,2,2,3,4,4] 
    # becomes [1,2,3,4], if the array is empty return null
    def removeDuplicates(self,arr):
        if arr==None:    
            return 0
        else:
            arr = list(dict.fromkeys(arr))
            return arr
    
    # returns true
    # returns false
    # equal
    # not equal
    
    # 2 arrays
    

    # This method returns true if array1 and array2 are equal
    # if they are not equal it returns false
    # arr1=[1,2,3,4] and arr2=[1,2,3,4] return true
    # arr1=[1,2,3,4] and arr2=[5,6,7,8] return false
        
    def isEqual(self,arr1,arr2):
        if (arr1 != arr2):
         return False

        else:
           arr1==arr2
        return True
        


    # This method returns the number of odd values inside the array
    # arr=[1,2,3,2] returns 2, if the array is empty return 0
        
    def numberOfOddNumbers(self,arr):
        if arr==None:
            return 0
        count=0
        # iterating each number in list
        for num in arr: 
      
        # checking condition
         if num % 2 != 0:
            count = count+1
        return count



    # This method returns the number of even values inside the array
    # arr=[1,2,3,2] returns 2, if the array is empty return 0
        
    def numberOfEvenNumbers(self,arr):
        if arr==None:
            return 0
        count=0
        # iterating each number in list
        for num in arr: 
      
        # checking condition
         if num % 2==0:
            count = count+1
        return count
        

    # This method returns the number of positive numbers in the array
    # if the array is empty return zero
    # arr=[1,2,-8,4] return 3
        
    def numberOfPositiveNumbers(self,arr):
        if arr==None:
            return 0
        count=0
        # iterating each number in list
        for num in arr: 
      
        # checking condition
         if num >= 0:
            count += 1
        return count
            

    # This method returns the number of negative numbers in the array
    # if the array is empty return zero
    # arr=[1,2,-8,4] return 1
    def numberOfNegativeNumbers(self,arr):
        if arr==None:
            return 0
        count=0
        # iterating each number in list
        for num in arr: 
      
        # checking condition
         if num < 0:
            count += 1
        return count
            

    # This method returns the most occuring value in the array
    # if the array is empty return zero
    # arr=[1,3,4,6,1,7,1,9] return 1
    def mostOccuring(self,arr):
        if arr==None:
            return 0
        count=0
        num=arr[0]
        # iterating each number in list
        for i in arr:

        # checking condition    
            curr_frequency = arr.count(i)
            if(curr_frequency> count):
             count = curr_frequency
             num = i
        return num

    # This method will sort the array by placing all 0's on the left of 
    # the array and 1's on the right side of the array and return the 
    # newly arranged array, arr=[1,0,1,0,1,0] returns [0,0,0,1,1,1]
        
    def sort(self,arr):
        if arr==None:
            return 0

        else:
            arr.sort()
        return arr