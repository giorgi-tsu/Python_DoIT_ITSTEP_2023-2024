# დავალება 27

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს 27 ლექციაზე, რომელიც ჩატარდა 
# 2024-03-14-ში და დავალების ჩაბარების ბოლო ვადაა 2024-03-21.

#******************************************************************#

print("\n",
      "-------------------- სავარჯიშო 1 --------------------", "\n")

## სავარჯიშო 1

# ფუნქცია ამოწმებს მარტივია თუ არა რიცხვი. 
# (მარტივია რიცხვი თუ ის მხოლოდ 1_ზე და საკუთარ თავზე იყოფა)
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# გატესტე ფუნქცია'unittest'_ის დახმარებით.

# დავალების ამოხსნა მოცემულია შემდეგ 2 ფაილში:

# prime_checker.py
# test_prime_checker.py


#------------------------------------------------------------------#