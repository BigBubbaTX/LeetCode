class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = digits.pop()
        c += 1
        digits.append(c)
        for i in range(1, len(digits)+1):
           
            if digits[-i] == 10:
                #del digits[-i]
                
                digits[-i] = 0
                #digits.insert(-i,0)
                print(digits)
              
                if len(digits) == 1:
                    digits.insert(0,1)
                elif -len(digits) == -i:
                        digits.insert(0,1)
                else:
                    print("act")
                    digits[-i -1] =digits[-i -1] +1

                    
            print(digits)
                

        return digits

