while True:
    try:
        data = input()
        replaceData = data.replace('BUG', '')
        while True:
            if data == replaceData:
                break
            data = replaceData
            replaceData = replaceData.replace('BUG', '')
        print(data)
    except:
        break