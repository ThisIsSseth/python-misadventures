#----____ Sets____-------------------------------
'''
Set items are unordered, unchangeable, and do not allow duplicate values.
The values True and 1 are considered the same value in sets
Same for false and 0
.add()
oldset.update(newIterable)
.remove(value)
If the item to remove does not exist, remove() will raise an error.
.discard(value)
Doesn't raise an error
.pop(index) pops randomly
.clear()
del _

The .union() and .update() methods joins all items from both sets.
You can use the | operator instead of the union() method
The .intersection() method keeps ONLY the duplicates. or use &

The .difference() method keeps the items from the first set that
are not in the other set(s). or use -   

The .symmetric_difference() method keeps all items EXCEPT the duplicates.
or use the ^

frozenset is an immutable version of a set.

copy() 	  	Returns a shallow copy 	
difference() 	- 	Returns a new frozenset with the difference 	
intersection() 	& 	Returns a new frozenset with the intersection 	
isdisjoint() 	  	Returns True if there is NO intersection between two frozensets 	
issubset() 	<= / < 	Returns True if this frozenset is a (proper) subset of another 	
issuperset() 	>= / > 	Returns True if this frozenset is a (proper) superset of another 	
symmetric_difference() 	^ 	Returns a new frozenset with the symmetric differences 	
union() 	| 	Returns a new frozenset containing the union

add() 	  	Adds an element to the set
clear() 	  	Removes all the elements from the set
copy() 	  	Returns a copy of the set
difference() 	- 	Returns a set containing the difference between two or more sets
difference_update() 	-= 	Removes the items in this set that are also included in another, specified set
discard() 	  	Remove the specified item
intersection() 	& 	Returns a set, that is the intersection of two other sets
intersection_update() 	&= 	Removes the items in this set that are not present in other, specified set(s)
isdisjoint() 	  	Returns True if NO items of this set is present in another set
issubset() 	<= 	Returns True if all items of this set is present in another set
  	< 	Returns True if all items of this set is present in another, larger set
issuperset() 	>= 	Returns True if all items of another set is present in this set
  	> 	Returns True if all items of another, smaller set is present in this set
pop() 	  	Removes an element from the set
remove() 	  	Removes the specified element
symmetric_difference() 	^ 	Returns a set with the symmetric differences of two sets
symmetric_difference_update() 	^= 	Inserts the symmetric differences from this set and another
union() 	| 	Return a set containing the union of sets
update() 	|= 	Update the set with the union of this set and others



'''