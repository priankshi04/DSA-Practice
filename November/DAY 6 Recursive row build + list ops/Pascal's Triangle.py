class Solution:
	def nthRowOfPascalTriangle(self, n):
	    # code here 
	    
	    #BRUTE FORCE
	    triangle=[]
	    for i in range(n):
	        row=[]
	        for j in range(i+1):
	                if j==0 or j==i:
	                    row.append(1)
	                else:
	                    value=triangle[i-1][j-1] + triangle[i-1][j]
	                    row.append(value)
	        triangle.append(row)
	    return triangle[n-1]
	    
	    #OPTIMAL
	    row=[1]
	    for i in range(1,n):
	        new_row= [1]
	        for j in range(1,i):
	            new_row.append(row[j-1]+row[j])
	        new_row.append(1)
	        row=new_row
	    return row
	                       
	            
	    
