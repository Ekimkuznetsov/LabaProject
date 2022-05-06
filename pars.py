import string

TOKEN_ALPHABETIC = {"A": string.ascii_uppercase,
                   "a": string.ascii_lowercase,
                   "d": string.ascii_digits,
                   "p": string.ascii_punctuation,
                   "-": "-",
                   "@": "@",
                    }

def pars(pattern: str) -> str:
    """
    recursion
    :param pattern: A%a%d%p%
    :return: Aadp
    """
    if len(pattern) == 0:
        return ""
    else:
        index = pattern.index("%")
        return TOKEN_ALPHABETIC[pattern[:index]] + pars(pattern[index+1:])

def pars1(pattern: str)-> str:
    tokens = pattern.split("%")
    return "".join(map(Lambda t: TOKEN_ALPHABETIC[t], tokens))











def pars2(pattern: str) -> list[dict]:
    token = {""
            "len": 0,
            "alph": ""
    }
    if len(pattern) == 0:
        return [token, ]
    else:
        if pattern[0] == "[":
            k = pattern.index("]")
            token["alph"] = pars1(pattern[1:k])
            pattern = pattern[k+1:]
        else:
            token["alph"] = TOKEN_ALPHABETIC[pattern[0]]
            pattern =
        token["alph"] = TOKEN_ALPHABETIC[pattern[0]]
        index = pattern.index("%)
        token["len"] = 1 if len(pattern[1:index]) == 0 else int(pattern[1:index])
        temp = pars2(pattern)
        return [token, ] + temp


if __name__ == "__main__":
    print(TOKEN_ALPHABETIC)
    print(pars("A%a%d%p%"))
    print(pars1("A%a%d%p%"))
    print(pars2("a45%d3%-%"))





    # a4%d3%-%[d%A%]5%-%[a%d%]4%@%[p%d%]4%