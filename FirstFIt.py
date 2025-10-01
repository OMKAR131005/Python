class display:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.list = [str1, str2]

    def __str__(self):
        return f"{self.str1} | {self.str2}"
def firstFit():
    process_size=[212,417,112,426]
    list_of_block_size=[100,500,300,600]

    print("process list:",process_size,"\n","list of memory:",list_of_block_size)
    Ans=[]
    for i in range(len(process_size)):
        for j in range( len(list_of_block_size)):
            if process_size[i]<list_of_block_size[j]:
                Ans.append(display(f"process {(process_size[i])} : is allocated to {list_of_block_size[j]} at index {j}",F"blockList is look like:{list_of_block_size}"))
                list_of_block_size[j] = list_of_block_size[j] - process_size[i]
                break
        if len(Ans)!=i+1:
                Ans.append(display(f"process {process_size[i]} : is not allocated", F"blockList is look like:{list_of_block_size}"))


    for i in Ans:
        print(i);
firstFit()