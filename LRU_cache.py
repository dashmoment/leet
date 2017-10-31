class obj_node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.pre = None
        self.next = None

        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = obj_node(None, None)
        self.tail = obj_node(None, None)
        
        self.head.next = self.tail
        self.tail.pre = self.head
        
        self.current_cap = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache: 
            self.cache[key].pre.next =  self.cache[key].next
            self.cache[key].next.pre =  self.cache[key].pre
            self.cache[key].pre = self.tail.pre
            self.tail.pre.next = self.cache[key] 
            self.cache[key].next = self.tail
            self.tail.pre = self.cache[key]
            
            return self.cache[key].value
        
        else:
            return -1
    

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache[key].value = value
            #sawp to tail
            self.cache[key].pre.next =  self.cache[key].next
            self.cache[key].next.pre =  self.cache[key].pre
            self.cache[key].pre = self.tail.pre
            
        else:
            if self.current_cap >= self.capacity:
                del_key = self.head.next.key
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
                self.cache.pop(del_key, None)
            else:
                self.current_cap +=1
            self.cache[key] =  obj_node(key, value)
                
        self.tail.pre.next = self.cache[key] 
        self.cache[key].next = self.tail
        self.cache[key].pre = self.tail.pre
        self.tail.pre = self.cache[key]
        
