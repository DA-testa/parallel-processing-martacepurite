# python3

def parallel_processing(n, m, data):
    output = []
    
    threads=[]
    time=0

    for i in range (n):
            threads.append(0)

    for i in range (m):

        for j in range(n):
             if(threads[j]==0):
                  if(len(data)>0):
                    threads[j]=data.pop(0)
                  else:break
                
                  toout=[j,time]
                  output.append(toout)

        for j in range(n):
            threads[j]=threads[j]-1

        time+=1
 
    return output

def main():

    inp=input().split()
    n = int(inp[0])
    m = int(inp[1])

    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(result[i][0],result[i][1])

if __name__ == "__main__":
    main()
