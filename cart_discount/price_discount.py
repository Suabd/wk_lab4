def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered three or more items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    
   #Check for number of Items
    if len(item_prices) < 3:
        return 0
    else:
        # If items more than 3 items, retrun priced items
        lowest_price = main(item_prices)
        return lowest_price


if __name__ == '__main__':
    main()
