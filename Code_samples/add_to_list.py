

def add_to_list(my_list):
   for i in range(len(my_list)):
       my_list[i] += 10
   return

if __name__ == "__main__":
   my_list = [1,2,3,4,5]
   print(add_to_list(my_list))
   print(my_list)