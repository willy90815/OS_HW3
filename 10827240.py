

class PageManager:
    def __init__(self):
        self.page_list = ""
        self.reslut_string = ''
        self.frame_size = 0
    def FIFO(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------FIFO-----------------------\n"
        frame = []
        for i in self.page_list:
            if i not in frame:
                if len(frame)>=self.frame_size:
                    del(frame[-1])
                    page_repalce+=1
                frame.insert(0,i)
                temp_str = "F"
                page_fault += 1
            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)+"\n\n"
    
    def LRU(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------LRU-----------------------\n"
        frame = []
        for i in self.page_list:
            if i not in frame:
                if len(frame)>=self.frame_size:
                    del(frame[-1])
                    page_repalce+=1
                frame.insert(0,i)
                temp_str = "F"
                page_fault += 1
            else:
                frame.remove(i)
                frame.insert(0,i)

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)+"\n\n"

    
    def LFU_LRU(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------Least Frequently Used LRU Page Replacement-----------------------\n"
        frame = []
        count = {}
        for i in self.page_list:
            
            if i not in frame: 
                if len(frame)>=self.frame_size:
                    temp= min(reversed(frame),key = lambda item:count[item])
                    count.update({temp:0})
                    frame.remove(temp)
                    page_repalce+=1
                frame.insert(0,i)
                count.update({i:1})
                temp_str = "F"
                page_fault += 1
            else:
                frame.remove(i)
                frame.insert(0,i)
                count.update({i:count[i]+1})
            

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)+"\n\n"
            
    def MFU_FIFO(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------Most Frequently Used Page Replacement-----------------------\n"
        frame = []
        count = {}
        for i in self.page_list:
            
            if i not in frame:
                if len(frame)>=self.frame_size:
                    temp= max(reversed(frame),key = lambda item:count[item])
                    count.update({temp:0})
                    frame.remove(temp)
                    page_repalce+=1
                frame.insert(0,i)
                count.update({i:1})
                temp_str = "F"
                page_fault += 1
            else:
                count.update({i:count[i]+1})
            

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)+"\n\n"
            
    def MFU_LRU(self):
        page_fault = 0
        page_repalce = 0
        self.reslut_string+="--------------Most Frequently Used LRU Page Replacement-----------------------\n"
        frame = []
        count = {}
        for i in self.page_list:
            
            if i not in frame:
                if len(frame)>=self.frame_size:
                    temp= max(reversed(frame),key = lambda item:count[item])
                    count.update({temp:0})
                    frame.remove(temp)
                    page_repalce+=1
                frame.insert(0,i)
                count.update({i:1})
                temp_str = "F"
                page_fault += 1
            else:
                frame.remove(i)
                frame.insert(0,i)
                count.update({i:count[i]+1})
            

            temp_str = i + '\t' + ''.join(frame)+'\t'+temp_str+"\n"
            self.reslut_string+= temp_str
            temp_str=""
        self.reslut_string+= "Page Fault = "+str(page_fault)+"  Page Replaces = "+str(page_repalce)+"  Page Frames = "+str(self.frame_size)+"\n"
    def set_reference(self, line, method, frame_size):
        self.page_list = line.removesuffix("\n")
        self.reslut_string = ''
        self.frame_size = int(frame_size)
        if method == "6":
            for i in range(5):
                self.sort(str(i+1))
        else:
            self.sort(method)

    def sort(self,method):
        if method == "1":
            self.FIFO()
        elif method == "2":
            self.LRU()
        elif method == "3":
            self.LFU_LRU()
        elif method == "4":
            self.MFU_FIFO()
        elif method == "5":
            self.MFU_LRU()
        else:
            print("method doesn't exist")
    def get_result(self):
        return self.reslut_string


    

filename = input("Enter \'quit\' to exit program \nEnter filename : ")
pm = PageManager()

while filename !="quit":
    filename = filename + ".txt"
    try:
        with open(filename) as file_in:
            first_line = file_in.readline()
            first_line = first_line.split()
            second_line = file_in.readline()
            pm.set_reference(method=first_line[0],frame_size=first_line[1],line=second_line )
        with open("out_"+filename,"w") as out_file:
            out_file.write(pm.get_result())
            print("\'\nout_"+filename+"\' is generated\n\n")
    except Exception as e: print(e)
    
    filename = ""
    filename = input("Enter \'quit\' to exit program \nEnter filename : ")
    
