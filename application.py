from flask import Flask, Response
from flask_restplus import Resource, Api, reqparse
from craigslist_emailer import SendEmail
from craigslist_parser import CraigslistParser
from craigslist_search import CLSearcher

application = Flask(__name__)
api = Api(application,
  version='1.0',
  title='CL API',
  description='CLl API',
)

craigslist_search = CLSearcher()
craigslist_parser = CraigslistParser()
emailer = SendEmail()

@api.route('/craigslist_search')
@api.doc(params={'search_term': 'the search term for the item you are looking for'})
class RunSearch(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('search_term')
        args = parser.parse_args()
        print (args)
        query = args['search_term']

        listings = craigslist_search.search(query)
        for listing in listings:
            url = listing['url']
            email = craigslist_parser.parse(url)
            message = emailer.generate_message(query, url)
            emailer.send_email('tylerdbecks@gmail.com', 'Interested in '+ str(query), message)
            # emailer.send_email(email, 'Interested in '+ str(query), message)
        

if __name__ == '__main__':
    application.run(debug=True)
