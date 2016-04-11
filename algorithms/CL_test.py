def mulit_maxProfit(prices):
    if(len(prices)<2):
        return 0
        
    bought_stock = False
    stock_price = 0
    profit = 0
        
    for i in range(len(prices)-1):
        cur_price = prices[i]
        next_price = prices[i+1]

        print i, 'if bought_stock:', bought_stock        
        print 'profit: ', profit        
        if(cur_price<next_price and bought_stock==False):
            bought_stock = True
            stock_price = cur_price
            
            if(i==(len(prices)-2)):
                profit += next_price - stock_price
                return profit
                
        elif(cur_price>next_price and bought_stock==True):
            profit += cur_price - stock_price
            bought_stock = False
            
        elif(cur_price<next_price and bought_stock==True and (i==(len(prices)-2))):
            profit += next_price - stock_price
            return profit
                
    return profit

def maxProfit(prices):
    curMax, curMin = prices[0], prices[0]
    MaxPrft = 0
    for i in range(1, len(prices)):

        if(prices[i]<curMin):
            Prft = curMax - curMin
            curMin = prices[i]
            curMax = prices[i]            
            MaxPrft = max(MaxPrft, Prft)
            continue

        if(prices[i]>curMax):
            curMax = prices[i]

        if(i==(len(prices)-1)):
            Prft = curMax - curMin
            MaxPrft = max(MaxPrft, Prft)


    return MaxPrft

    

data = [1, 2, 8, 5, 4, 2, 6]

print maxProfit(data)
