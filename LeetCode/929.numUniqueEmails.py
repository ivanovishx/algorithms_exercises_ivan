929.numUniqueEmails.py
class Solution:





    #O(N)

    def numUniqueEmails(self, emails: [str]) -> int:
    res = []
    # res = set()
    for email in emails:
        name, domain = email.split('@')
        name = name.split('+')[0].replace('.', '')
        res.append(name + '@' + domain)
        # res.add(name + '@' + domain)
    return len(set(res))









    # O(N2)
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        dictionary_names = {}
        for email in emails:
            at = email.find('@')
            filter_name = ""
            for char in email[:at]:
                if char == '+':
                    break
                elif char == '.' :
                    pass`
                else:
                    filter_name += char
            
            filter_name += email[at:]
            print (filter_name)
            
            # dictionary_names[filter_name] 
            
            if filter_name in dictionary_names:
                dictionary_names[filter_name] += 1
            else:
                dictionary_names[filter_name] = 0
            
        return len(dictionary_names)