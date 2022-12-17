'''
SList Module
CS2420 Data Structures and Algorithms
Author: Tate Thomas


Sorted doubly-linked list class:

    Methods:

    __init__(contents): can take none or more elements, separated by a comma.
        If a different SList is passed in, all the contents within will be
        transferred over to new SList, along with any other args. All types of
        objects are valid elements.
    insert(value): inserts 1 value into list, while maintaining
        non-decreasing order. If a different SList is passed in, all the contents
        will be inserted.
    index(value): finds the index of the given value and returns it. If the value
        does not exist in the list, it will return None.
    find(value): finds the given value in the list and returns the node for it. If
        it is not found, it will return None.
    remove(value): removes the first occurance of the given value. If a different SList
        is passed in, each value in the SList will be checked for removal from original
        list. Returns True if an item was removed, False if no items were removed.
    remove_all(value): removes all occurances of the given value in the list. If a
        different SList is passed in, each value in the SList will be used to remove
        each occurance in the original list. There is no return value.
    change_sorting(obj_type, method): changes the sorting method for strings or built-in
        lists for the current SList object. obj_type can either be str or list.
        method is an int. String methods: 0=length, 1=alphabetical order, 2=ascii total.
        List methods: 0=length, 1=order, 2=total. SList is resorted with new method afterwards.
        There is no return value.
    size(): returns the length of the list.

    Magic methods:

    __str__(): returns a string in [a, b, c] format, with string objects surrounded in ''.
    __iter__(): SList is iterable. Invoked by using the format: for node in SList.
    __getitem__(index): SList can be indexed. Invoked by using the format: list[index].
        SList can be indexed in reverse, using a negative number, with -1 being the last item.
    __len__(): SList keeps track of the length of the list. Invoked by using
        the format: len(list). 

SList Node class:

    Attributes:

    self.value = value held by the node.
    self.next = reference to the next node in the list.
    self.back = reference to the node behind itself in the list.

    Magic Methods:

    __str__(): returns self.value as a string.
    __getitem__(index): if a list is held in self.value, you can use the format: node[index].
    __instancecheck__(clss): the value held by Node can be instance checked.
    ALL COMPARISON OPERATORS ARE IMPLEMENTED (value is compared).
    ALL MATH OPERATORS ARE IMPLEMENTED (value is used).
'''

class SList:
    '''SList class:
    Sorted doubly-linked list. All types of objects can be held.

    Methods:
    __init__(contents)
    insert(value)
    index(value)
    find(value)
    remove(value)
    remove_all(value)
    change_sorting(obj_type, method)
    size()
    '''


    _str_choice = 0    # 0: length, 1: alphabetical order, 2: ascii total
    _list_choice = 0    # 0: length, 1: order, 2: total


    class SListNode:
        '''SListNode class:
        Node for SList. Holds the value, pointer to next node, and pointer to node behind itself.

        Attributes:
        self.value
        self.next
        self.back
        '''

        def __init__(self, value = None, nexxt = None, back = None):
            '''Can take a value, next node, and last node. All default to None'''
            self.value = value
            self.next = nexxt
            self.back = back

        def __str__(self):
            '''Returns the value of the node as a string'''
            return f"{self.value}"

        def __getitem__(self, index):
            '''Returns the value at given index in a list that's being held by the node'''
            return self.value[index]

        def __instancecheck__(self, clss):
            '''Returns a bool. Checks self.value's type'''
            return isinstance(self.value, clss)

        def __getattr__(self, name):
            '''Helps function calls work for classes that are being held by self.value'''
            def method(*args):
                return getattr(self.value, f"{name}")(*args)
            return method

        def _find_float_val(self, value):
            '''Returns the value in a comparable float form'''
            return SList._find_float_val(self, value)

        def __lt__(self, value):
            '''Compares value of node to the given value'''
            val1, val2 = self._find_float_val(self.value), self._find_float_val(value)
            return val1 < val2

        def __gt__(self, value):
            '''Compares value of node to the given value'''
            val1, val2 = self._find_float_val(self.value), self._find_float_val(value)
            return val1 > val2

        def __eq__(self, value):
            '''Compares value of node to the given value'''
            val1, val2 = self._find_float_val(self.value), self._find_float_val(value)
            return val1 == val2

        def __le__(self, value):
            '''Compares value of node to the given value'''
            return not self.__gt__(value)

        def __ge__(self, value):
            '''Compares value of node to the given value'''
            return not self.__lt__(value)

        def __ne__(self, value):
            '''Compares value of node to the given value'''
            return not self.__eq__(value)

        def __add__(self, value):
            '''Performs operation with value of node and the given value'''
            if isinstance(value, SList.SListNode):
                return self.value + value.value
            return self.value + value

        def __sub__(self, value):
            '''Performs operation with value of node and the given value'''
            if isinstance(value, SList.SListNode):
                return self.value - value.value
            return self.value - value

        def __mul__(self, value):
            '''Performs operation with value of node and the given value'''
            if isinstance(value, SList.SListNode):
                return self.value * value.value
            return self.value * value

        def __floordiv__(self, value):
            '''Performs operation with value of node and the given value'''
            if isinstance(value, SList.SListNode):
                return self.value // value.value
            return self.value // value

        def __truediv__(self, value):
            '''Performs operation with value of node and the given value'''
            if isinstance(value, SList.SListNode):
                return self.value / value.value
            return self.value / value

        def __mod__(self, value):
            '''Performs operation with value of node and the given value'''
            if isinstance(value, SList.SListNode):
                return self.value % value.value
            return self.value % value

        def __pow__(self, value):
            '''Performs operation with value of node and the given value'''
            if isinstance(value, SList.SListNode):
                return self.value ** value.value
            return self.value ** value

        def __float__(self):
            '''Returns the node's value as a float'''
            return float(self.value)


    class IterableList:
        '''Iterator class'''
        def __init__(self, lyst):
            '''Takes a list to turn into iterator'''
            self.current_node = None
            self.next_node = lyst._head
        def __next__(self):
            '''Iterates to next value, stops when it hits None'''
            if self.next_node is None:
                raise StopIteration
            self.current_node = self.next_node
            self.next_node = self.next_node.next
            return self.current_node


    def __init__(self, contents = None, *args):
        '''Can take any type of value, defaults to None. Multiple values can
        be passed using the format: SList(a, b, c). If an SList is used in
        initialization, all the contents of that list will be inserted into
        new SList
        '''

        self._head = None
        self._tail = None
        self._size = 0

        if len(args) == 0:
            if contents is not None:
                # only 1 item was provided
                self.insert(contents)
        else:
            # multiple items provided
            self.insert(contents)
            for arg in args:
                self.insert(arg)


    def _find_float_val(self, value):
        '''Finds a float value for the input for a comparison'''

        def alph_vals(string):
            '''Finds the ascii value of each character and returns a list of those values'''
            new = []
            for let in string:
                new.append(ord(let))    # append ascii value to new
            return new

        if isinstance(value, SList.SListNode):
            # value given is a node
            return self._find_float_val(value.value)

        if isinstance(value, str):
            # find float val based on str method
            if self._str_choice == 0:
                return float(len(value))
            if self._str_choice == 1:
                return alph_vals(value)
            alph_list = alph_vals(value)
            total = 0   # total of all ascii characters
            for let in alph_list:
                total += let
            return float(total)

        if isinstance(value, int):
            return float(value)

        try:
            iter(value)     # check if value is iterable

            # find float val based on list method
            if self._list_choice == 0:
                return float(len(value))
            if self._list_choice == 1:
                new = []
                for val in value:
                    new.append(self._find_float_val(val))
                return new
            total = 0
            for val in value:
                total += self._find_float_val(val)
            return float(total)

        except:
            return float(value)


    def insert(self, value):
        '''Inserts a new value/values(if an SList is given) into the list.
        Maintains nondecreasing ordering of elements. If a pair of elements
        are the same, the newer one will appear after. Sorting method of
        strings and built-in lists are customizable, using
        self.change_sorting(obj_type, method). No return value
        '''

        if isinstance(value, SList):
            for val in value:
                self.insert(val.value)

        else:
            if self._head is None:
                # list is empty
                new = SList.SListNode(value)
                self._head = new
                self._tail = new

            else:
                for curr in self:
                    # find location of insert value

                    insert_val = self._find_float_val(value)    # float representations
                    curr_val = self._find_float_val(curr.value)
                    i = 0   # index where value should be inserted

                    if isinstance(curr_val, list) and isinstance(insert_val, list):
                        try:
                            while True:
                                # replacing lists with float values
                                if curr_val[i] < insert_val[i]:
                                    curr_val = 0.0
                                    insert_val = 1.0
                                    break
                                if curr_val[i] > insert_val[i]:
                                    curr_val = 1.0
                                    insert_val = 0.0
                                    break
                                i += 1
                        except:
                            curr_val = float(len(curr_val))
                            insert_val = float(len(insert_val))

                    elif isinstance(curr_val, list) and not isinstance(insert_val, list):
                        try:
                            while True:
                                if curr_val[i] != insert_val:
                                    curr_val = float(curr_val[i])
                                    break
                                i += 1
                        except:
                            curr_val = insert_val

                    elif isinstance(insert_val, list):
                        try:
                            while True:
                                if curr_val != insert_val[i]:
                                    insert_val = float(insert_val[i])
                                    break
                                i += 1
                        except:
                            insert_val = curr_val

                    if insert_val < curr_val:
                        new = SList.SListNode(value, curr, curr.back)
                        if curr.back is None:
                            self._head = new
                        else:
                            curr.back.next = new
                        curr.back = new
                        break

                    if curr.next is None:
                        new = SList.SListNode(value, None, curr)
                        curr.next = new
                        self._tail = new
                        break

            self._size += 1


    def index(self, value):
        '''Searches for a value in the list, return index if found, None otherwise.
        If an SList is passed through, it will search for a matching subset of the list,
        returning the index of the first value
        '''

        index = 0   # index of self

        if isinstance(value, SList):
            n = 0   # index of value
            while index < len(self):
                if n == len(value):
                    return index - n    # gives the index of the first value
                if isinstance(value[n].value, type(self[index].value)) and (value[n] == self[index]):
                    # same type and same value
                    n += 1
                else:
                    index -= n # go to the index after where SList first matched
                    n = 0
                index += 1

        else:
            for num in self:
                if isinstance(num.value, type(value)) and (num.value == value):
                    return index
                try:
                    if num.value.__instancecheck__(type(value)) and (num.value == value):
                        return index
                except:
                    pass
                index += 1

        return None


    def find(self, value):
        '''Searches for a value in the list, return the node if found, None otherwise'''

        lyst_index = self.index(value)
        if lyst_index is None:
            return None
        return self[lyst_index]


    def remove(self, value):
        '''Removes the first occurance of value/values(if an Slist is given).
        Returns True if a value is removed, False if no value is removed
        '''

        if isinstance(value, SList):
            ret_bool = False    # return bool
            for val in value:
                result = self.remove(val.value)
                if result is True:
                    ret_bool = True
            return ret_bool

        index = self.index(value)
        if index is None:
            return False

        node = self[index]
        self._size -= 1
        prev = node.back
        front = node.next

        if prev is None:
            node.next.back = None
            self._head = front
        else:
            prev.next = front

        if front is None:
            prev.next = None
            self._tail = prev
        else:
            front.back = prev

        del node
        return True


    def remove_all(self, value):
        '''Removes all instances of value/values(if an SList is given). No return value'''

        if isinstance(value, SList):
            for val in value:
                self.remove_all(val.value)

        else:
            if isinstance(value, SList.SListNode):
                num = value.value
            else:
                num = value
            result = True
            while result:
                result = self.remove(num)


    def size(self):
        '''Returns the length of the list as an int'''

        return len(self)


    def change_sorting(self, obj_type, method):
        '''Changes the sorting method of the specified type (str, list).
        String methods: 0=length, 1=alphabetical order, 2=ascii total.
        List methods: 0=length, 1=order, 2=total. SList is resorted with new method afterwards.
        There is no return value.
        '''

        if (method < 0) or (method > 2) or not isinstance(method, int):
            raise AttributeError(f"{method} is not a valid sorting method (use int 0-2)")

        re_sort = SList()
        if obj_type is str:
            for elem in self:
                if isinstance(elem.value, str):
                    re_sort.insert(elem.value)
            self._str_choice = method

        elif obj_type is list:
            for elem in self:
                if isinstance(elem.value, list):
                    re_sort.insert(elem.value)
            self._list_choice = method

        else:
            raise TypeError("{obj_type} does not have a sorting method")

        self.remove(re_sort)
        self.insert(re_sort)
        del re_sort


    def __str__(self):
        '''Converts the list into a string form and returns it'''

        if len(self) <= 0:
            return "[]"

        convert = "["
        for curr in self:
            if isinstance(curr.value, str):
                convert += f"'{curr.value}', "
            else:
                try:
                    # try instance check again
                    if curr.value.__instancecheck__(str):
                        convert += f"'{curr.value}', "
                    else:
                        raise
                except:
                    convert += f"{curr.value}, "

        convert = convert[:-2] + "]"
        return convert


    def __iter__(self):
        '''Returns an iterator for the list'''

        return SList.IterableList(self)


    def __getitem__(self, index):
        '''Returns the item at the given index, throws an exception if invalid index'''

        if not isinstance(index, int):
            raise IndexError(f"{type(index)} cannot index a list")

        if index >= 0:
            curr = self._head
            for _ in range(index):
                curr = curr.next
                if curr is None:
                    raise IndexError(f"list[{index}] is not a valid index")

        else:
            curr = self._tail
            for _ in range((index * -1) - 1):
                curr = curr.back
                if curr is None:
                    raise IndexError(f"list[{index}] is not a valid index")

        return curr


    def __len__(self):
        '''Returns the length of the list'''

        return self._size
