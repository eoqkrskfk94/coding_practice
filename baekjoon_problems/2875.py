f_student, m_student, i_student = map(int, input().split())
left_male = 0
while True:
  if f_student >= m_student * 2:
    left_female = f_student - m_student * 2
    if left_female + left_male >= i_student:
      print(m_student)
      break
    else:
      m_student -= 1
      left_male += 1
  else:
    m_student -= 1
    left_male += 1
