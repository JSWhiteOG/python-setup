def hello(hi):
  print("Hello, my name is computer")

def pack(a,b,c):
  return [a,b,c]


def eat_lunch(firstItem):
 if len(firstItem) == 0:
    print("My lunchbox is empty!")
 else:
    for i in range(len(firstItem)):
      if i == 0:
        print(f"First I eat {firstItem[0]}")
      else:
        print(f"Next I eat {firstItem[i]}")

