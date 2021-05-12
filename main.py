import pafy

url = input('Введите URL для скачивания:\n')

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

        count_steam = int(input('Введите номер:\n'))
        downld = steams[count_steam - 1].download() 

        print(f'Видео "{paf.title}" успешно скачено')

    except Exception as e:
        print(f'Ошибка\n{e}')

download(url)