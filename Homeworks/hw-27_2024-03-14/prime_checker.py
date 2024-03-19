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