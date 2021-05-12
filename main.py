import pafy

url = input('Enter URL to download:\n')

def download(url):
    try:
        paf = pafy.new(url)
        steams = paf.streams
        avalivable_steams = {}
        count = 1
    
        for steam in steams:
            avalivable_steams[count] = steam
            print(f'{count}. {steam}')
            count+=1

        count_steam = int(input('Enter a number:\n'))
        downld = steams[count_steam - 1].download() 

        print(f'Video "{paf.title}" has been successfully downloaded')

    except Exception as e:
        print(f'Error\n{e}')

download(url)
