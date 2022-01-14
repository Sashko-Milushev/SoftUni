number_of_lines = int(input())
stack_of_queries = []
for _ in range(number_of_lines):
    queries = input().split()
    type_of_queries = queries[0]
    if type_of_queries == '1':
        number = int(queries[1])
        stack_of_queries.append(number)
    elif type_of_queries == '2' and stack_of_queries:
        stack_of_queries.pop()
    elif type_of_queries == '3' and stack_of_queries:
        print(max(stack_of_queries))
    elif type_of_queries == '4' and stack_of_queries:
        print(min(stack_of_queries))

while stack_of_queries:
    element = stack_of_queries.pop()
    if not stack_of_queries:
        print(element)
    else:
        print(element, end=', ')

