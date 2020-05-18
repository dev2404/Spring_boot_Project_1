class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class link_list:
	def __init__(self):
		self.head = None

	def append(self,data):
		new_node = node(data)
		if self.head is None:
			self.head=new_node
			return

		last_node = self.head
		while last_node.next is not None:
			last_node = last_node.next
		last_node.next = new_node	

	def display(self):
		curr = self.head
		while curr:
			print(curr.data)
			curr=curr.next
	
	def prepend(self, data):
		new_node = node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after(self, prev_node , data):
		new_node = node(data)
		if  not prev_node:
			print("prev_node is not in the list")
			return
		new_node.next  = prev_node.next
		prev_node.next = new_node 

	def delete_head(self, data):
			curr_head = self.head
			if curr_head and curr_head.data == data:
				self.head = curr_head.next
				curr_head = None
				return

			prev = None
			while curr_head and curr_head.data != data:
				prev = curr_head
				curr_head = curr_head.next

			if curr_head is None:
				return

			prev.next = curr_head.next
			curr_head = None	
	
	def delete_node(self, pos):
		curr_head = self.head
		prev = None
		count = 1
		if pos == 0:
			self.head = curr_head.next
			curr_head = None
			return
		while curr_head and count != pos:
			prev = curr_head
			curr_head = curr_head.next
			count += 1 
		if curr_head is None:
			return
		
		prev.next = curr_head.next
		curr_head = None

	def len_iterative(self):
		curr = self.head
		count = 0
		while curr:
			curr = curr.next
			count=count+1
		return count	

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)	

	def swap(self, key_1, key_2):
		prev_1 = None
		curr_1 = self.head
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next

		prev_2 = None
		curr_2 = self.head
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next
		if not curr_1 or not curr_2:
			return
		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2
		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1
		curr_1.next, curr_2.next = curr_2.next, curr_1.next	

	def merge_sorted(self, ll_2):
			p = self.head
			q = ll_2.head
			s=None
			if not p:
				return q
			if not q:
				return p

			if p and q:
				if p.data <= q.data:
					s = p
					p = s.next
				else:
					s = q
					q = s.next
			new_head = s
			while p and q:
				if p.data <= q.data:
					s.next = p
					s = p
					p = s.next
				else:
					s.next = q
					s = q
					q = s.next
			if not p:
				s.next = q
			if not q:
				s.next = p 
			return new_head

	def dublicate(self):
		prev = None
		curr=self.head
		dup_values = dict() 
		while curr:
			if  curr.data  in dup_values:
				prev.next = curr.next
				curr = None 
			else:
				dup_values[curr.data] = 1
				prev = curr
			curr = prev.next
	def n_t0_n(self):
		curr = self.head
		while curr.next.next is not None:
			curr = curr.next
		print(curr.data)	

	def count_occurances_iter(self, data):
		curr = self.head
		count = 0
		while curr:
			if curr.data == data:
				count = count+1
			curr = curr.next
		return count

	def count_occurances_recu(self, node, data):
		if not node:
			return 0

		if node.data == data:
			return 1 + self.count_occurances_recu(node.next, data)
		else:
			return self.count_occurances_recu(node.next, data)

	def rotate(self, k):
		p = self.head
		q = self.head
		prev = None
		count = 0
		while p and count < k:
			prev = p
			p = p.next
			q = q.next
			count = count+1
		p = prev
		#print(p.data)
		while q:
			prev = q
			q = q.next
		q = prev
		#print(q.data)
		
		q.next = self.head
		self.head = p.next
		p.next = None

	def palindrome(self):
		curr = self.head
		#s = ""
		#while curr:
		#	s += curr.data
		#	curr = curr.next
		#return s == s[::-1]

		s = []
		while curr:
			s.append(curr.data)
			curr=curr.next
		curr = self.head 
		while curr:
			data = s.pop()
			if curr.data != data:
				return False
			curr=curr.next
		return True	

	def addintion(self, llist):
		p = self.head
		q = llist.head

		sum_list = link_list()

		carry = 0
		while p or q:
			if not p:
				i=0
			else:
				i=p.data
			if not q:
				j=0
			else:
				j=q.data

			s = i + j + carry
			print("s:" + str(s))
			if s >= 10:
				carry = 1
				remainder = s%10
				sum_list.append(remainder)
			else:
				carry = 0
				sum_list.append(s)
			if p:
				p = p.next
			if q:
				q = q.next
		sum_list.display()		 






				
				



			




ll = link_list()
ll_2 = link_list()

ll.append(5)
ll.append(6)
ll.append(3)
#ll.append("R")  
#ll.insert_after(ll.head.next, "e")
#ll.delete_head("b")
#ll.delete_node(3)
#print(ll.len_iterative())
#print(ll.len_recursive(ll.head))
#ll.swap("c", "a")

ll_2.append(8)
ll_2.append(4)
ll_2.append(2)

#ll.merge_sorted(ll_2) 	
#ll.dublicate()
#ll.display()
#ll.n_t0_n()
#print(ll.palindrome())
ll.addintion(ll_2)
print(365+248)
#print(ll_2.palindrome())
#ll.rotate(4)
#ll_2.display()
#print(ll.count_occurances_iter(2))
#print(ll.count_occurances_recu(ll.head, 3))
				