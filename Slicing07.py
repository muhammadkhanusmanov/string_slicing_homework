def main(s,n):
    """
   The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int ): parameter
    Returns:
        str: answer
    """
    if n>=0:
        m = s[:len(s)-n]
    else:
        m = s[-n:]
    return m 
