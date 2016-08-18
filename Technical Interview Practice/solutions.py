"""Technical Interview Practice (Python) Project"""
# Q1
print "### Question 1 ###"
def question1(s=None, t=None): # Defaults are None to return False instead of error
    """Main function of question 1"""
    if isinstance(s, str) is False or isinstance(t, str) is False or \
    len(t) > len(s) or len(s) == 0 or len(t) == 0:
        return False

    s = s.lower() # make string lower case for consistency
    t = t.lower() # make string lower case for consistency
    t_dict = dict.fromkeys(t, 0) # convert t into unordered dict

    l = len(s)
    for i in xrange(l):
        for j in xrange(i, l):
            temp_string = s[i:j + 1]
            if dict.fromkeys(temp_string, 0) == t_dict:
                return True
    return False

# Q1 Test Case
# Test Case 1
print question1("udacity", "ad")
# output should be True
# Test Case 2
print question1("u", "u")
# output should be True
# Test Case 3
print question1("uity", "dsfsfasfsDFASDG")
# output should be False
# Test Case 4
print question1("uity", 123)
# output should be False
# Test Case 5
print question1("udacity", None)
# output should be False
# Test Case 6
print question1(True, 123)
# output should be False
# Test Case 7
print question1()
# output should be False

# Q2
print "\n### Question 2 ###"
def question2(a=None): # Default is None to return warning instead of an error
    """Main function of question 2"""
    if isinstance(a, str) is False:
        print "This is not a string."
        return None
    elif len(a) == 1:
        return a
    elif len(a) < 1:
        print "This is not an appropriate string."
        return None

    a = a.lower() # make string lower case for consistency
    output = a[0] # if string only consists unique chars then return first char
    for i in range(len(a)):
        for j in range(i):
            temp = a[j:i + 1]
            if temp == temp[::-1] and len(temp) > len(output): #check if reverse is same
                output = temp
    return output

# Q2 Test Case
# Test Case 1
print question2("qpoakazakquumpolop")
# output should be kazak
# Test Case 2
print question2("")
# output should be None with a error message.
# Test Case 3
print question2("a")
# output should be a
# Test Case 4
print question2(1235)
# output should be None with a error message.
# Test Case 5
print question2(True)
# output should be None with a error message.
# Test Case 6
print question2()
# output should be None with a error message.
# Test Case 7
print question2("qpoakakquumpollop")
# output should be pollop
# Test Case 8
print question2("pollop")
# output should be pollop
# Test Case 9
print question2("abc")
# output should be a

# Q3
print "\n### Question 3 ###"
def question3(G):
    """Main function of question 3"""
    if is_valid_graph(G) is False:
        print "Input is not appropriate."
        return None
    nodes, edges = input_converter(G)
    from collections import defaultdict
    import heapq
    conn = defaultdict(list)
    for n1, n2, c in edges:
        conn[n1].append((c, n1, n2))
        conn[n2].append((c, n2, n1))

    mst = []
    used = set(nodes[0])
    usable_edges = conn[nodes[0]][:]
    heapq.heapify(usable_edges)

    while usable_edges:
        cost, n1, n2 = heapq.heappop(usable_edges)
        if n2 not in used:
            used.add(n2)
            mst.append((n1, n2, cost))

            for e in conn[n2]:
                if e[2] not in used:
                    heapq.heappush(usable_edges, e)
    return output_converter(mst)

def input_converter(G):
    """This function is to convert the input format that the main function can read"""
    nodes = []
    edges = []
    for key in G.keys():
        nodes.append(key)
    for key in G.keys():
        for i in G[key]:
            edges.append((key, i[0], i[1]))
    return nodes, edges

def output_converter(mst):
    """This function is to reconvert the output of the main function into appropriate format"""
    G = {}
    for i in mst:
        if i[0] not in G.keys():
            G[i[0]] = []
        if i[1] not in G.keys():
            G[i[1]] = []
        G[i[0]].append((i[1], i[2]))
        G[i[1]].append((i[0], i[2]))
    return G

def is_valid_graph(G=None):
    """This function is to check the format of the input if appropriate"""
    if isinstance(G, dict) is False:
        return False
    elif isinstance(G, dict):
        for val in G.values():
            if isinstance(val, list) is False or len(val) == 0:
                return False
            for i in val:
                if isinstance(i, tuple) is False or len(i) != 2 or \
                isinstance(i[0], str) is False or isinstance(i[1], int) is False:
                    return False
        return True

# Q3 Test Case
# Test Case 1
G = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
print question3(G)
# output should be {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
# Test Case 2
G = {'A': [('B', 2), ('G', 5)],
     'B': [('A', 2), ('C', 10), ('E', 20)],
     'C': [('B', 10), ('E', 1), ('D', 4)],
     'D': [('C', 4), ('F', 3)],
     'F': [('G', 2), ('E', 9), ('D', 3)],
     'E': [('B', 20), ('F', 9), ('C', 1)],
     'G': [('A', 5), ('F', 2)]}
print question3(G)
# output should be {'A': [('B', 2), ('G', 5)], 'C': [('D', 4), ('E', 1)], 'B': [('A', 2)],\
# 'E': [('C', 1)], 'D': [('F', 3), ('C', 4)], 'G': [('A', 5), ('F', 2)], 'F': [('G', 2), ('D', 3)]}
# Test Case 3
G = {'A': [('B', 2, 5)], 'B': [('A', 2), "Q", ('C', 5)], 'C': [('B', 5)]}
print question3(G)
# output should be None with a error message.
# Test Case 4
print question3(None)
# output should be None with a error message.

# Q4
print "\n### Question 4 ###"
def question4(T, r, n1, n2):
    """Main function of question 4"""
    if input_checker_q4(T, r, n1, n2) is False:
        print "Input is not appropriate"
        return None
    root = r
    while (root > n1 and root > n2) or (root < n1 and root < n2):
        if root > n1 and root > n2:
            for i in T[root][:root]:
                if i == 1:
                    root = T[root][:root].index(i)
        elif root < n1 and root < n2:
            for i in T[root][root+1:]:
                if i == 1:
                    root = T[root][root+1:].index(i) + root + 1
    return root

def input_checker_q4(T, r, n1, n2):
    """This function is to check the format of the input if appropriate"""
    if isinstance(T, list) and isinstance(r, int) and \
    isinstance(n1, int) and isinstance(n2, int) and \
    r <= len(T) and n1 <= len(T) and n2 <= len(T):
        if all(isinstance(i, list) and len(i) == len(T) for i in T):
            return bool(all(all(j == 0 or j == 1 for j in i) for i in T))
        else:
            return False
    else:
        return False

# Q4 Test Case
# Test Case 1
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]], 3, 1, 4)
# output should be 3
# Test Case 2
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]], 3, 0, 2)
# output should be 1
# Test Case 3
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]], 3, 4, 6)
# output should be 5
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]], 3, 1, 4)
# Test Case 4
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 2, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]], 3, 0, 2)
# output should be None with a error message.
# Test Case 5
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]], 3, 4, 6)
# output should be None with a error message.
# Test Case 6
print question4("ASd", 3, 1, 4)
# output should be None with a error message.
# Test Case 7
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]], 3, 0, 239999999999999)
# output should be None with a error message.
# Test Case 8
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]], 3, "asd", 6)
# output should be None with a error message.
# Test Case 9
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]], 3, "asd", None)
# output should be None with a error message.

# Q5
print "\n### Question 5 ###"
def question5(ll, m):
    """Main function of question 5"""
    if input_checker_q5(ll, m) is False:
        print "Input is not appropriate."
        return None

    # find the length of the list
    temp = ll.head
    list_length = 0
    while temp:
        temp = temp.next
        list_length += 1

    if m > list_length:
        print "Input is not appropriate."
        return None

    # then find the mth element from the end
    temp = ll.head
    for i in range(list_length-m):
        temp = temp.next
    return temp.data

def input_checker_q5(ll, m):
    """This function is to check the format of the input if appropriate"""
    return bool(isinstance(ll, LinkedList) and isinstance(m, int))

class Node(object):
    """Class for nodes"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    """Class for LinkedList"""
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """This function is to append element to linkedlist"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

# Q4 Test Case
# Set up some Elements
e1 = Node(100000)
e2 = Node(4)
e3 = Node(9)
e4 = Node(2)
e5 = Node(25)
e6 = Node(99)
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)

# Test Case 1
print question5(ll, 4)
# output should be 9
# Test Case 2
print question5(ll, 1)
# output should be 99
# Test Case 3
print question5(ll, 6)
# output should be 100000
# Test Case 4
print question5(ll, "asd")
# output should be None with a error message.
# Test Case 5
print question5(7, 6)
# output should be None with a error message.
# Test Case 6
print question5(ll, None)
# output should be None with a error message.
# Test Case 7
print question5(ll, 699999999999999999999)
# output should be None with a error message.
