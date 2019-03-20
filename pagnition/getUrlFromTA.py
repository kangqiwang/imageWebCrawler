import requests

downloadFileName="/home/sourcemogul4/Projects/source-mogul/imageWebCrawler/pagnition/generateUrl/generateFromTA.csv"
downloadLink="https://www.facebook.com/tr/?id=118020122088261&ev=SubscribedButtonClick&dl=https%3A%2F%2Fwww.tacticalbucket.com%2Fdashboard%2Fget-categories%2F1000bulbs.com&rl=https%3A%2F%2Fwww.tacticalbucket.com%2Fdashboard%2Fcategories-list%2Fta&if=false&ts=1552904828174&cd[buttonFeatures]=%7B%22classList%22%3A%22btn%20btn-default%20btn-facebook%22%2C%22destination%22%3A%22https%3A%2F%2Fwww.tacticalbucket.com%2Fdashboard%2Fget-categories%2F1000bulbs.com%23%22%2C%22id%22%3A%22%22%2C%22imageUrl%22%3Anull%2C%22innerText%22%3A%22Select%20All%22%2C%22name%22%3A%22%22%2C%22numChildButtons%22%3A0%2C%22tag%22%3A%22a%22%7D&cd[buttonText]=Select%20All&cd[formFeatures]=%5B%5D&cd[pageFeatures]=%7B%22title%22%3A%22Bulk%20Category%20Generator%20-%20Tacticalbucket%22%7D&sw=1600&sh=900&ud[em]=14d446042338234319a31a68acba51ddad6add3388ba4025da102039419ad446&v=2.8.42&r=stable&ec=3&o=30&fbp=fb.1.1549466536441.402472324&it=1552904825295&coo=false&es=automatic&rqm=GET"

data=requests.get(downloadLink)
print(data.content)
# file = open(downloadFileName, 'wb')
# file.write(data)
# file.close()