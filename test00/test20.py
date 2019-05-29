def isPalindrome(string):
    # letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    # tmp = ''
    # raw_string = string.lower()
    # for char in raw_string:
    #     if char in letters:
    #         tmp += char
    # if ''.join(list(reversed(tmp))) == tmp:
    #     return True
    # return False
    s_filter = ''.join(filter(str.isalnum, string)).lower()
    return s_filter[::-1] == s_filter


if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    flag = isPalindrome(string)
    print(flag)
