from pystack import *
st=Stack()
print(dir(st))
try:
    st.peek()
except StackEmpty as exc:
    print(exc)
st.push([])
print(type(st.pop()))
for i in ['1',1,[1.0],1,dict(a=1)]:
    st.push(i)
while True:
    print(st.pop())
