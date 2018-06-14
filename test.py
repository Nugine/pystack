from pystack import *
st=Stack()
print(dir(st))
try:
    st.peek()
except StackEmpty as exc:
    print(exc)
for i in range(100):
    st.push(i)
while True:
    print(st.pop())
