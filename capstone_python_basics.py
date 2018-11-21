import requests
from bs4 import BeautifulSoup
import statistics


# function that will scrape links off of a web-page
# that's entered in the parameter as page
def crawl_web_page(page):
    r = requests.get(page)

    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a')

    # finds actual web pages address and strips off the http or the https://www
    page_links = []
    for linker in links:
        if 'https://www' in linker['href']:
            page_links.append(linker['href'][12:])

        elif 'https://' in linker['href']:
            page_links.append(linker['href'][8:])

        elif 'http://www' in linker['href']:
            page_links.append(linker['href'][11:])

        elif 'http://' in linker['href']:
            page_links.append(linker['href'][7:])

    # strips off extra after original web page
    stripped_page_links = []
    for linker in page_links:
        end_of_page = linker.find("/")
        stripped_page_links.append(linker[:end_of_page])

    return stripped_page_links


# list of author's web pages
web_pages_1 = ['https://marksullivanbooks.com/','http://www.alexrose.com/men-of-war/',  'https://a16z.com/author/ben-horowitz/', 'https://www.mortenhansen.com/', 'http://johnferling.com/books/', 'https://www.facebook.com/MalcolmGladwellBooks/', 'https://mindsetonline.com/abouttheauthor/','http://bobwoodward.com/', 'https://www.ericschumacher.net/', 'http://ryanbeckerwrites.com/author/ryanb/', 'http://www.briankilmeade.com/', 'http://eriklarsonbooks.com/', 'https://www.aspeninstitute.org/our-people/walter-isaacson/', 'http://www.jonmeacham.com/books/', 'https://doriskearnsgoodwin.com/books/', 'http://johndavidmann.com/books/', 'https://ronchernow.com/books/', 'http://thomasflemingwriter.com/', 'https://www.andrew-roberts.net/', 'https://www.billoreilly.com/', 'https://www.adammakos.com/', 'https://robertvaughan.com/books/', 'http://www.wendyholden.com/', 'http://www.simonandschusterpublishing.com/davidmccullough/', 'https://www.elinhilderbrand.net/','http://jennaglatzer.com/bio/', 'http://www.markdagostino.com/home.html','https://www.kerryanneking.com/', 'https://www.cg-cooper.com/novels.html', 'https://ashleyfarley.com/ashley-farley-books/', 'http://www.samanthachristy.com/books2.html', 'http://www.shaynesilvers.com/', 'http://www.jenikasnow.com/bookshelf/', 'https://www.rachelhauck.com/', 'http://www.juliannemaclean.com/', 'https://www.maryburton.com/novels/', 'http://www.helenhardt.com/book/', 'https://www.jodipicoult.com/', 'https://ltryan.com/', 'http://janewashington.com/', 'http://www.johnsandford.org/', 'http://www.kevinkwanbooks.com/', 'http://rhysbowen.com/', 'http://www.jim-butcher.com/', 'https://www.laurakamoie.com/', 'http://www.stephaniedray.com/', 'http://www.michaelcrichton.com/', 'http://powerseductionandwar.com/' ,'http://www.dianagabaldon.com/', 'http://jamiebeck.com/', 'https://brenebrown.com/', 'https://www.teresadriscoll.com/', 'https://www.deliaowens.com/', 'https://www.kendraelliot.com/home/', 'https://www.evanovich.com/', 'http://www.neilgaiman.com/', 'https://melindaleigh.com/', 'http://lianemoriarty.com.au/', 'https://www.johnmaxwell.com/', 'https://penelopewardauthor.com/','http://www.michaelgrantbooks.co.uk/', 'https://www.eoincolfer.com/books','https://margaretweis.com','http://www.trhickman.com/', 'http://www.suzannecollinsbooks.com/','http://laurahillenbrandbooks.com/about-laura/','http://www.storyman.com/', 'http://www.johngreenbooks.com/', 'http://www.richardpaulevans.com/', 'https://www.pcwrede.com/about-patricia/', 'http://www.karenwitemeyer.com/','https://www.jenturano.com/books/','http://www.melissatagg.com/','http://shannaswendson.com/','http://www.robert-ludlum.com/','https://sarahladd.com/', 'https://www.madeleinelengle.com/', 'http://www.louislamour.com/','http://julieklassen.com/', 'http://www.deehenderson.com/', 'https://www.catherinecoulter.com/books-and-series', 'http://maryhigginsclark.com/', 'http://allycarter.com/', 'https://ptbradley.com/', 'https://clive-cussler-books.com/','https://www.agathachristie.com/','https://wimpykid.com/', 'https://www.traciabramson.com/', 'https://www.jkrowling.com/', 'http://rickriordan.com/', 'http://www.josiskilpack.com/', 'http://www.roseannamwhite.com/', 'http://www.jamespatterson.com/all-books#.W_N3J-hKg2w','https://www.davidbaldacci.com/landing-page/david-baldacci-books/', 'https://www.stephenking.com/', 'https://www.arthurconandoyle.com/', 'https://www.hemingwayhome.com/', 'http://www.georgerrmartin.com/', 'http://www.jgrisham.com/books/', 'http://annerice.com/', 'https://www.deankoontz.com/', 'https://brandonsanderson.com/', 'https://www.anthonyhorowitz.com/', 'http://www.tashaalexander.com/', 'http://terriblackstock.com/']

print(len(web_pages_1))
# runs each web page through web-scraper and pulls all
# the links into list called biggest_list
biggest_list = []
for page in web_pages_1:
    mini_linklist = crawl_web_page(page)
    for link in mini_linklist:
        biggest_list.append(link)


# sorts through biggest_list and makes a dictionary with
# webpages as the keys and number of times it appears
# as the values. Each key SHOULD be unique
link_dictionary = {}
for link in biggest_list:
    if link in link_dictionary:
        link_dictionary[link] += 1
    else:
        link_dictionary[link] = 1


# Creates list of dictionary values so we can find median
num_times_list = []
for value in link_dictionary:
    num_times = link_dictionary[value]
    num_times_list.append(num_times)

median = statistics.median(num_times_list)


# sort key/value pairs into two lists: one upper 2 quartiles, other lower two quartiles.
# values exactly equal to the median will be included in the lower grouping
most_frequent = []
least_frequent = []

for key, value in link_dictionary.items():
    if value > median:
        most_frequent.append(key)
    elif value <= median:
        least_frequent.append(key)


print("The most frequently used links are: ")
for link in most_frequent:
    print(link)

print("---------------------------------------------------------------------------------")

print("The least frequently used links are: ")
for link in least_frequent:
    print(link)


