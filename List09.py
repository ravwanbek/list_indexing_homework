def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer

    """
    
    
    if list1.count(list1[0])==len(list1):
        return True
    else: 
        return False
print(main([8,8,8,8,8,9,8]))
