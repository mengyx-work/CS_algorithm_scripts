import heapq
hq_objects = []
hq_tuples = []

class Item(object):
    def __init__(self, priority, content):
        self.priority = priority
        self.content = content

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

    def __str__(self):
        return 'priority: {}, content: {}'.format(self.priority, self.content)

## add objects into the heapq
contents = [Item(2, 'tt'), Item(5, 'bb'), Item(2, 'dd')]
for content in contents: 
    heapq.heappush(hq_objects, content)
    heapq.heappush(hq_tuples,(content.priority, content))

print 'object pops: ', heapq.heappop(hq_objects)
#print hq_tuples
content = heapq.heappop(hq_tuples)
print content[1]

