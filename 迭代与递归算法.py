"""for 循环 同时要练习输入输出"""
def sum(n:int) -> int:
  """for 循环"""
  ans = ()
  for i in range(n):
    ans += i
  return ans
if _name_ = "_main_":
    n = 5
    ans = sum(n)
    print(f"\n for循环的求和结果为ans={ans}")
    
