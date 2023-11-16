def concatenate_strings(str1, str2):
    """
    두 문자열을 연결하는 함수

    Parameters:
    - str1 (str): 첫 번째 문자열
    - str2 (str): 두 번째 문자열

    Returns:
    - str: 연결된 문자열
    """
    result = str1 + str2
    return result

# 예시
string1 = "Hello, "
string2 = "world!"
result_string = concatenate_strings(string1, string2)
print(result_string)
