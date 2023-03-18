# python3



def parallel_processing(n, m, data):
    output = []
    
    threads=[]
    time=0

    for i in range (n):
            threads.append(0)
            ##print(i,end=" ")
            ##print(threads[i],end=" ")
            
            

    ##print()
        
    for i in range (m):
        

        for j in range(n):
             if(threads[j]==0):
                  if(len(data)>0):
                    threads[j]=data.pop(0)
                  else:break
                  
                  ##print("threadindtakesjob: ",end=" ")
                  toout=[j,time]
                  output.append(toout)
                  ##print(j,end=" ")
                  ##print("time: ",end=" ")
                  ##print(time,end=" ")
                  ##print()
        

        for j in range(n):
            threads[j]=threads[j]-1
            ##print("thrproc: ",end=" ")
            ##print(threads[j],end=" ")
            
        ##print()
        time+=1
            


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    inp=input().split()
    n = int(inp[0])
    m = int(inp[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(result[i][0],print(result[i][1])
        
        

    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
