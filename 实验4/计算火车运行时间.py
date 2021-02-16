begin,end = input().split()
s_begin = begin[:2]
m_begin = begin[2:]
s_end = end[:2]
m_end = end[2:]
s_begin = int(s_begin)
m_begin = int(m_begin)
s_end = int(s_end)
m_end = int(m_end)
x = m_end - m_begin
if x>=0 :
    print("{:0>2}:{:0>2}".format((s_end - s_begin),(x)))
else:
    print('{:0>2}:{:0>2}'.format((s_end - s_begin-1),(x+60)))