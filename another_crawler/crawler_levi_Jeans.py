
'''
511™ Slim Fit Stretch Jeans
WaterLess
$59.99

crawl custumers's reviews
After running this source, it will create to file cmt_custumer.csv
The product's link:
https://www.levi.com/US/en_US/clothing/men/jeans/511-slim-fit-stretch-jeans/p/045112369?fbclid=IwAR0FBoKxkWg3PB4NsbJpZpdFZHnfBkaYSFyMFe29SjOkEfpw0ef2DZn7f_k
'''

import requests, json, codecs
import webbrowser


webbrowser.open('045112369-front-pdp.jpg')

def get_fix(i, limit):
    return '&filter.q' + str(i) + '=productid:eq:045112369&include.q' + str(i) + '=comments&limit.q'+str(i)+'=' + str(limit)

limit = 100

api_url = 'https://api.bazaarvoice.com/data/batch.json?passkey=ca68iFuyCSvgNcQbyjzgnsURQlXrJrJQn10w3kChiZPK4&apiversion=5.5&resource=reviews'

try:
    api_responds =  requests.get(api_url + get_fix(0, limit)).content
except AssertionError as error:
    print(error)

result = json.loads(api_responds)
result = result['BatchedResults']['q0']['Results']

fname = './cmt_custumer.csv'
with codecs.open(fname, 'w', encoding='utf8') as fout:
	fout.write('Id,UserNickname,Rating,Title,ReviewText' + '\n')

	for subresult in result:
		fout.write(str(subresult['Id']) + ',' + str(subresult['UserNickname']) + ',' + str(subresult['Rating']) + ',\"' + subresult['Title'] + '\",\"' + subresult['ReviewText']+ '\"' + '\n')
