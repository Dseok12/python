def prt_cone_vol(r,h) :
  if r > 0 and h > 0 :
    vol = 1/3 * 3.14 * r ** 2 * h
    print("원뿔의 부피는", vol, "입니다.")
  else :
    print("반지름과 높이는 양수여야 합니다.");

prt_cone_vol(20,30);

digits = 54321;
def reverse_digits(digits) :
  while digits != 0 :
    digit = digits % 10
    print(digit, end="")
    digits //= 10
reverse_digits(digits)