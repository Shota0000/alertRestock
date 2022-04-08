total=0
def test_func():
    global total
    loops=20
    for i in range(loops):
        total+= 10

print(total)
test_func()
print(total)

score=[20,40,80,90]
total=0
for i in score:
    total+=i
print(total)
print(sum(score))