from newsplease import NewsPlease

def print_hi(name):

    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('PyCharm')

    article = NewsPlease.from_url(
        'https://www.cnn.com/2024/04/16/politics/donald-trump-trial-narrative-analysis/index.html')
    print(article.text)

